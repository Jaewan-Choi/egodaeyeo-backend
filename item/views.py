from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q
from item.pagination import PaginationHandlerMixin
from item.serializers import ItemSerializer, CategorySerializer, DetailSerializer
from egodaeyeo.permissions import IsAddressOrReadOnly
from user.models import User as UserModel
from item.models import (
    Item as ItemModel,
    Category as CategoryModel,
    Bookmark as BookmarkModel,
)


class ItemPagination(PageNumberPagination): # 👈 PageNumberPagination 상속
    page_size = 12

class ItemListView(APIView, PaginationHandlerMixin):
    permission_classes = [IsAddressOrReadOnly]
    authentication_classes = [JWTAuthentication]
    pagination_class = ItemPagination
    
    def get(self, request):
        user = request.user
        items = ItemModel.objects.filter(status="대여 가능").order_by('-created_at')
        categories = CategoryModel.objects.all()
        
        #유저가 주소를 설정 했을때 Query
        try:
            address_query = Q(user__address__contains=user.address) & ~Q(user=user)
            items = items.filter(address_query)
        except:
            pass
        
        # 카테고리명 Query Parameter로 가져오기
        category_name = request.GET.get('category', "")
        # 섹션 Query Parameter로 가져오기
        section = request.GET.get('section', "")
        
        if category_name != "":
            category_query = Q(category__name=category_name)
            items = items.filter(category_query)
            
        if section != "":
            section_query = Q(section=section)
            items = items.filter(section_query)
            
        page = self.paginate_queryset(items)
        
        if page is not None:
            item_serializer = self.get_paginated_response(ItemSerializer(page,many=True).data)
        else:
            item_serializer = ItemSerializer(items, many=True)
        
        category_serializer = CategorySerializer(categories, many=True, context={"request": request})
        data = {
            'categories': category_serializer.data,
            'items': item_serializer.data,
        }
        return Response(data, status=status.HTTP_200_OK)
        

# 아이템 상세페이지 뷰
class DetailView(APIView):
    permission_classes = [IsAddressOrReadOnly]
    authentication_classes = [JWTAuthentication]

    # 페이지 접속시
    def get(self, request, item_id):
        
        try:
            item = ItemModel.objects.get(id=item_id)
        # 아이템 정보가 없을 시
        except:
            return Response({'error_msg': '아이템 정보가 없습니다'}, status=status.HTTP_404_NOT_FOUND)

        login_id = request.user.id
        detail_serializer = DetailSerializer(item, context={'login_id': login_id})

        return Response(detail_serializer.data, status=status.HTTP_200_OK)

    # 찜하기 버튼 클릭시
    def post(self, request, item_id):
        user_id = request.user.id
        user = UserModel.objects.get(id=user_id)
        item = ItemModel.objects.get(id=item_id)

        try:
            # 북마크 모델 존재 여부 체크
            bookmark_model_check = BookmarkModel.objects.get(user=user_id, item=item_id)
            # 북마크 모델 있을시 삭제
            bookmark_model_check.delete()
            # 로그인 유저 북마크 여부
            is_bookmark = False
            # 북마크 갯수 카운터
            bookmark_length = BookmarkModel.objects.filter(item=item_id).count()

            return Response({'is_bookmark': is_bookmark, 'bookmark_length': bookmark_length}, status=status.HTTP_200_OK)


        # 북마크 모델 없을시 저장
        except:
            new_bookmark = {
                'user': user,
                'item': item
            }
            BookmarkModel.objects.create(**new_bookmark)
            # 로그인 유저 북마크 여부
            is_bookmark = True
            # 북마크 갯수 갱신
            bookmark_length = BookmarkModel.objects.filter(item=item_id).count()
            return Response({'is_bookmark': is_bookmark, 'bookmark_length': bookmark_length}, status=status.HTTP_201_CREATED)

