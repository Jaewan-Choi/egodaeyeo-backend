## 프로젝트
<img width="350" alt="Screen Shot 2022-08-05 at 6 55 15 PM" src="https://user-images.githubusercontent.com/102135145/185027151-60ad490c-6a83-43a1-abde-bcdc4da396c7.png">
배포 사이트 : https://www.egorental.com<br>
주제 : 당근마켓 모티브 개인 간 대여 서비스 플랫폼<br>
일정 : 2022.07.07 ~ 2022.08.16<br>
개발 인원 : 3인<br><br>

프론트엔드 깃헙 링크 : https://github.com/MeoSeon12/egodaeyeo-frontend<br>
백엔드 깃헙 링크 : https://github.com/MeoSeon12/egodaeyeo-backend<br>
S.A 링크 : https://quixotic-wok-871.notion.site/S-A-3183ff7202e942099238af3effd956ea

<br>

## 1. 기술 스택
* ### 백엔드
  * Python 3.9
  * Django 4.0
  * Django Rest Framework 3.13
  * Django Rest Framework simple-jwt 5.2.0
  * Django Channels 3.0.5
  * Docker 20.10.12
  * Nginx 1.22.0
  * Gunicorn 20.1.0
  * Daphne 3.0.2

* ### 프론트엔드
  * Websocket
  * HTML5
  * Javascript
  * JQuery
  * CSS
  
* ### 데이터베이스
  * AWS RDS PostgreSQL
  * AWS S3

* ### 배포
  * AWS EC2
  * AWS Route 53
  * Github Actions
  * Netlify
<br>

## 1-1. 기술 스택 선정 이유
* **Django / DRF**
  > Serializer, 유저 관리, REST API 등 Django에서 제공하는 다양한 기능들을 사용하기 위해 채용
* **Django Channels**
  > 실시간 비동기로 들어오는 ws/wss 프로토콜을 장고에서 대응하기 위해 사용
* **Django Rest Framework simple-jwt**
  > 유저 인증을 토큰방식으로 암호화하기 위해 사용
* **Websocket**
  > 실시간 채팅 기능 구현에 있어 채팅을 칠 때마다 매번 HTTP 통신을 하는 것은 느리고 비효율적이기 때문에 실시간 비동기 프로토콜을 제공하는 웹소켓 기술을 사용
* **Netlify**
  > 가장 간편하고 비용 지불없이 정적 웹사이트 호스팅이 가능하며, 특별한 설정없이 깃헙과도 동기화되므로 사용
* **AWS EC2**
  > 용량을 줄이거나 늘릴 수 있는 탄력성을 가지고 있고, 보안 및 네트워크 구성, 스토리지 관리에 효과적이며 간단한 프로젝트 배포를 프리티어로 무료로 이용할 수 있다는 점에서 채용
* **AWS S3**
  > 서비스에서 이미지를 업로드 할때, EC2에 저장을 하게되면 용량이 부족해지고 파일들을 관리하기가 어렵습니다. 그래서 파일 저장에 최적화 되어있고, 저장용량이 무한대에 가까운 S3를 사용해서 이미지 파일들을 저장하고 관리 했습니다.
* **Github actions**
  > 프로젝트가 업데이트 될 때마다 수동으로 배포 서버를 업데이트 해야하는 불편함을 개선하기 위해 깃헙과 자동으로 동기화를 지원하는 깃헙 액션을 채용
* **Docker**
  > Docker는 소프트웨어를 컨테이너라는 표준화된 유닛으로 패키징하는데, 컨테이너에는 라이브러리, 시스템 도구, 코드, 런타임 등 소프트웨어를 실행하는데 필요한 모든것이 포함되어 있습니다. 이러한 특징을 가진 Docker를 활용해서 환경에 구애받지 않고 애플리케이션을 신속하게 배포 및 확장하고 규모가 달라져도 안정적으로 저렴하게 애플리케이션을 구축, 제공 및 실행 하기위해 사용했습니다.
* **Nginx**
  > event-driven의 비동기 구조인 특징을 가지고 있는 nginx는 채팅기능 때문에 동시접속자 수의 증가에 대응하기에 적합한 방식의 웹서버라고 생각했습니다. 또한 무중단 배포가 가능하여 채팅기능이 있는 웹사이트에서 배포시 중단되지 않는점이 사용자들에게 사용성 및 편의성을 증대시킵니다.
* **Gunicorn**
  > 로컬개발환경에서는 django의 runserver를 사용하여 gunicorn이 없어도 유용하게 사용 할 수 있지만, 배포환경에서는 runserver를 사용하지 않도록 django에서도 권장되어있습니다. 그래서 Python WSGI 대표적으로 성능이 검증된 Gunicorn을 활용해서 Nginx로부터 받은 서버사이드 요청을 gunicorn을 활용해서 django로 전달하게끔 했습니다.
* **Daphne**
  > Gunicorn이 WSGI HTTP요청을 처리한다면 저희 서비스에 있는 채팅기능은 ASGI WS 요청을 처리해야 합니다. Daphne는 Channels 를 설치하면 자동으로 설치되며 Channels에서 지원하는 서버로 ASGI 프로토콜로 받은 WS요청을 처리하려고 사용했습니다.
* **PostgreSQL**
  > PostgreSQL은 MySQL보다 표준에 더 가깝게 구현하는것을 목표로 두고있고, 오픈소스 및 커뮤니티가 이끄는 데이터베이스 입니다. django에서 가장 권장하는 RDBMS가 PostgreSQL이었기 때문에 이를 직접 사용해봄으로써 MySQL과는 어떠한 차이점이 있는지 공부도 하고, 다른 RDBMS를 사용해봄으로써 경험치를 쌓고자 사용했습니다.

<br>

## 2. API 명세서
<a href="https://documenter.getpostman.com/view/20826963/VUqymsv9#intro">포스트맨 DOCS 바로가기</a>

<br>

## 3. DB 설계 ERD
https://www.erdcloud.com/d/zfZo5E3pKdEorSGBX
<img src="https://user-images.githubusercontent.com/104349901/185032482-c6b7c6c8-a164-4b71-8318-ba74ef12a1d5.png">

<br>

## 4. 담당 작업 (최재완)

* 채팅 기능 (공동 작업 with 김규민)

  - 개별 채팅방 오픈 시 개별 채팅방의 ID값을 활용해 채팅방 마다 다른 웹소켓 주소에 연결
  - 채팅 작성 혹은 거래 상태 업데이트 시 send()로 데이터를 백엔드에 전송
  - Django Channels의 @database_sync_to_async 데코레이터와 create() 메소드로 데이터를 DB에 저장
  - 채팅 그룹으로 데이터를 전송하고 sender 값을 체크하여 작성자와 수신자에 맞게 레이아웃을 보여줌
  - 채팅방을 닫거나 다른 채팅방 오픈 시 기존 접속 채팅 웹소켓 websocket.close() 메소드를 사용하여 연결을 끊음
  
* 알림 기능

  - 로그인 시 유저 고유의 웹소켓 주소로 연결
  - 채팅을 보낼 때 수신 유저의 웹소켓 주소로 send()
  - Django Channels로 wss 프로토콜(ASGI)을 처리
  - 채팅 메시지 DB 모델에 is_read 필드를 추가하여 읽은 여부를 판단 후 알림을 보냄
  - 수신자는 onmessage()를 통해 응답 데이터를 처리
  - 채팅을 읽으면 is_read 필드를 True로 수정
  
* 물품 등록 / 수정 / 삭제

  - 사용자의 인풋값을 받은 폼데이터를 POST 요청을 통해 DB에 저장
  - 프론트에서는 인풋의 포맷에 제한 두기, null 체크 등을 진행
  - 백엔드에서는 벨리데이션을 통해 모델에 적합한 데이터인지 검사
  - 수정 시 게시글의 ID값을 활용하여 GET 요청으로 DB에 저장된 데이터를 활용
  - 수정 시 최종적으로 수정된 데이터를 PUT 요청을 통해 DB에 반영
  - 삭제 시 작성자 본인 여부를 토큰의 payload와 DB의 데이터를 교차검증을 통해 체크 후 삭제
  
* 프론트 배포

  - Netlify로 정적 호스팅하여 배포
  - 프로젝트 front-End Github 의 main 브랜치와 자동으로 동기화
  - 네임서버를 추가하여 구매한 도메인 적용
  
* 다크모드 (공동 작업 with 김철현)

  - 로그인 유저의 로컬 스토리지에 다크모드 여부를 저장
  - 로컬스토리지의 다크모드 값을 if문의 분기점으로 다른 스타일을 적용
  
* 메인페이지 웰컴 박스와 스크롤 기능

  - 웰컴 박스 레이아웃 작업
  - scrollTop 메소드에서 offset().top 으로 스크롤을 이동

<br>

역할은 팀장으로서 참여하였고, 프로젝트 발표 또한 담당하였습니다<br>
담당 작업의 프론트와 백엔드 모두 작업하였습니다<br>

<br>

## 5. 핵심 기능
### 5-1. 채팅과 알림 기능
담당한 작업 중에서 첫번째 핵심 기능은 채팅과 알림 기능입니다<br>
사용자 간 실시간 채팅과 알림, 그리고 사이트 이용에 필수적인 물품 대여 문의부터 리뷰를 남기는 기능까지<br>
모두 채팅에서 이루어질 수 있도록 설계되어있습니다<br>

Websocket의 wss 프로토콜을 이용하여 서버와 통신하고 서버에서는 Django의 Channels 라이브러리를 사용하여 비동기 요청을 처리합니다<br>

채팅 기능과 알림 기능 둘 다 로직은 비슷하며,<br>
채팅은 개별 채팅방마다 다른 주소를 사용하고 채팅창을 열었을 때만 해당 웹소켓에 연결하고 닫으면 끊어지지만,<br>
알림 기능은 로그인 시 웹소켓에 연결하고 계속해서 연결을 유지하고 있는 차이점이 있습니다<br>

<details markdown="1">
 <summary>코드 설명 보기</summary>
  <br>
		
  * 클라이언트가 비동기 요청 보낼 때
  > 웹소켓의 .send() 메소드를 사용하여 비동기 요청을 보냅니다
  ```js
  // 알림 웹소켓 보내기
  sendAlert(roomId, senderId, receiverId, contractStatus) {
      // 상대방에게 채팅 알림 보냄
      chatAlertSocket.send(JSON.stringify({
          'room_id': roomId,
          'sender': senderId,
          'receiver': receiverId,
          'status': contractStatus,
          'created_at': Date.now(),
      }))
  }
  ```
  <a href="https://github.com/MeoSeon12/egodaeyeo-frontend/blob/5c695571da923125f00fd8df82d2111e01a75137/index/js/chat.js#L695">코드 보러가기</a>
  <br><br>

  * 서버에서 비동기 요청을 처리하고 응답할 때
  > Django Channels 라이브러리를 활용하여 웹소켓의 연결, 요청, 재가공, 응답, 종료를 처리합니다
 
  ```py
  class AlertConsumer(AsyncConsumer):

    async def websocket_connect(self, event):

        user_id = self.scope['url_route']['kwargs']['user_id']
        chat_alert = f'user_chat_alert_{user_id}'
        self.chat_alert = chat_alert

        await self.channel_layer.group_add(
            chat_alert,
            self.channel_name
        )
        await self.send({
            'type': 'websocket.accept'
        })

    # 웹소켓에 데이터 들어옴
    async def websocket_receive(self, event):

        received_data = json.loads(event['text'])
        receiver_id = received_data.get('receiver')

        # 데이터 가공
        sender = await self.get_user_object(received_data['sender'])  # 작성자 닉네임
        title = await self.get_title_object(received_data['room_id'])

        # 수신자에게 보낼 데이터
        response = {
            'sender': sender,
            'title': title,
            'room_id': received_data['room_id'],
            'status': received_data['status'],
            'created_at': received_data['created_at']
        }

        # 수신자에게 온메시지에 보냄
        other_user_chat_alert = f'user_chat_alert_{receiver_id}'

        await self.channel_layer.group_send(
            other_user_chat_alert,
            {
                'type': 'chat_message',
                'text': json.dumps(response)
            }
        )

    # 웹소켓 연결종료
    async def websocket_disconnect(self, event):
        pass

    async def chat_message(self, event):
        await self.send({
            'type': 'websocket.send',
            'text': event['text'],
        })

    # 데이터 가공 (발신자 닉네임 조회)
    @database_sync_to_async
    def get_user_object(self, sender_id):
        qs = User.objects.get(id=sender_id)
        return qs.nickname

    # 데이터 가공 (채팅창 제목 조회)
    @database_sync_to_async
    def get_title_object(self, room_id):
        qs = ChatRoom.objects.get(id=room_id)
        return qs.item.title
  ```
  <a href="https://github.com/Jaewan-Choi/egodaeyeo-backend/blob/5d7870b682646070adf40cbfa1d7caab39fa6ba3/chat/consumers.py#L212">코드 보러가기</a>
  <br><br>
  
  * 클라이언트가 서버에서 응답을 받을 때
  > 웹소켓은 onmessage 메소드를 사용하여 서버에서 응답한 데이터를 처리합니다
  
  ```js
  // 알림 수신
  chatAlertSocket.onmessage = function (e) {
      // 알림 데이터
      let data = JSON.parse(e.data)
      if (chatSocket.url != `${webSocketBaseUrl}/chats/${data.room_id}`) {
          ....
      }
  ```
  <a href="https://github.com/MeoSeon12/egodaeyeo-frontend/blob/5c695571da923125f00fd8df82d2111e01a75137/index/js/chat.js#L656">코드 보러가기</a>
</details>

<br>

### 5-2. 이미지 첨부 및 수정
물품 등록 및 수정 페이지에서 이미지를 최대 5개, 총 50MB까지 첨부가 가능하도록 설계했습니다<br>
이미지를 첨부하면 각각의 미리보기와 파일제목 목록이 나타나며, 개별적으로 제거 혹은 추가가 가능합니다<br>

<details markdown="1">
 <summary>코드 설명 보기</summary>
  <br>

  * 이미지 첨부 및 제거
  > file 객체에 담은 단일 혹은 복수의 이미지 파일을 리스트로 구성하여 인덱스를 통해 각각의 이미지에 접근하여 제거가 가능하며,<br>
  > 리스트로 append 하여 이미 첨부한 파일 리스트에 추가로 첨부가 가능합니다<br>
  > 이미지 제거 시 리스트에서 인덱스가 달라지는 것을 고려하여,<br>
  > 리스트에서 완전히 제거하는 것이 아닌 'is_delete' 키를 추가하여 최종적으로 서버로 전달할 것인지 판단합니다

```js
let fileNo = 0  // 이미지 마다 다른 id를 지정해주기 위함
let filesArr = []  // 업로드한 이미지들을 담을 파일 리스트

// 이미지 첨부 시
function imgUpload(obj) {
    let maxFileCnt = 5   // 첨부파일 최대 개수
    let attFileCnt = document.querySelectorAll('.filebox').length    // 기존 추가된 첨부파일 개수
    let remainFileCnt = maxFileCnt - attFileCnt    // 추가로 첨부가능한 개수
    let curFileCnt = obj.files.length  // 현재 선택된 첨부파일 개수
    
    // 첨부파일 개수 확인
    // 최대 개수 초과 시
    if (curFileCnt > remainFileCnt) {
        alert("이미지는 최대 " + maxFileCnt + "개 까지 첨부 가능합니다.")
    }

    // 최대 개수 넘지 않았을 시
    else {
        for (const file of obj.files) {
            const prImg = document.getElementById('pr-img')
            prImg.style.display = 'grid'
            
            // 파일 배열에 담기
            var blob = file.slice(0, file.size, 'image/png')
            newFile = new File([blob], `${file.name.split('.')[0]}-${(new Date / 1)}.png`, { type: 'image/png' })
            filesArr.push(newFile)

            // 이미지 미리보기
            let img = new Image()
            img.src = URL.createObjectURL(file)
            
            let previewHtmlData = img
            previewHtmlData.setAttribute('id', `preview-img-${fileNo}`)
            $('.file-input-custom').before(previewHtmlData)
            
            // 이미지 목록에 추가
            let htmlData = ''
            htmlData += '<div id="file' + fileNo + '" class="filebox">'
            htmlData += '   <p class="name">' + file.name + '</p>'
            htmlData += '   <a class="delete" onclick="deleteFile(' + fileNo + ')">❌</a>'
            htmlData += '</div>'
            $('.file-list').append(htmlData)

            fileNo++
        }
    }
}

// 첨부파일 삭제 
function deleteFile(num) {
    document.querySelector("#file" + num).remove()
    document.querySelector("#preview-img-" + num).remove()
    filesArr[num].is_delete = true
}
```
<a href="https://github.com/MeoSeon12/egodaeyeo-frontend/blob/5c695571da923125f00fd8df82d2111e01a75137/item/js/upload.js#L18">코드 보러가기</a>
<br><br>

* 서버에서 전달받은 데이터 처리
> 폼데이터로 게시글의 여러 인풋과 이미지 리스트가 함께 들어오는데,<br>
> DB 구조 상 글 내용과 이미지를 따로 저장할 필요가 있어<br>
> 각각 벨리데이션을 진행하고 결과에 따라 다른 응답을 보내줍니다<br>
> 
> 내용이 먼저 저장되고 이미지 벨리데이션이 통과되지 않는 경우에는<br>
> 기존에 저장된 내용을 삭제하는 트랜잭션 기능도 구현해보았습니다

```py
# 물품 등록하기 기능
def post(self, request):

    # 중략...

    item_serializer = ItemPostSerializer(data=item_data)

    # 아이템 모델 벨리데이션 합격하면 저장
    if item_serializer.is_valid():
        item_obj = item_serializer.save()

        # 이미지 포함하는지 체크
        if not 'image' in request.data:
            return Response(item_obj.id, status=status.HTTP_200_OK)
        else:
            images = request.data.pop('image')

            passed_item_image_data_list = []
            for image in images:
                item_image_data = {
                    'item': item_obj.id,
                    'image': image,
                }

                item_image_serializer = ItemImageSerializer(data=item_image_data)

                # 아이템 이미지 모델 벨리데이션 합격하면 합격 리스트에 추가
                if item_image_serializer.is_valid():
                    passed_item_image_data_list.append(item_image_serializer)

                # 아이템 이미지 모델 벨리데이션 불합격하면 아이템 모델 삭제
                else:
                    item_obj.delete()
                    return Response(item_image_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            # 모든 이미지가 벨리데이션에 합격했다면 저장
            for passed_item_image_data in passed_item_image_data_list:
                passed_item_image_data.save()

            return Response(item_obj.id, status=status.HTTP_200_OK)

    # 아이템 모델 벨리데이션 불합격
    else:
        return Response(item_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```
<a href="https://github.com/Jaewan-Choi/egodaeyeo-backend/blob/2b38b3cff3b877e3d9a7d8830d25ad74f1ab4a2d/item/views.py#L160">코드 보러가기</a>
</details>

<br>

## 6. 트러블 슈팅
### 6-1. 채팅이 모든 채팅방에 공유가 되는 문제
<details markdown="1">
 <summary>자세한 내용 보기</summary>
  <br>
  
  * 문제 : 
  	* 페이지 로딩 시 채팅 웹소켓에 연결하도록 하였는데, 그러다보니 모든 채팅방이 하나의 웹소켓을 사용하여 채팅이 공유되는 문제 발생했습니다
  * 해결 : 
  	* 채팅 웹소켓 연결을 페이지 로딩 시가 아닌 개별 채팅방을 열 때 연결시켰습니다
  	* 채팅방을 닫거나, 다른 채팅방을 열면 기존에 접속한 웹소켓을 끊었습니다
	  ```js
	  async function openChatRoom(roomId) {
	    // 이미 접속한 채팅, 거래 웹소켓이 있다면 종료
	    if (chatSocket != '' && contractSocket != '') {
		chatSocket.close()
		contractSocket.close()
		chatSocket = ''
		contractSocket = ''
	    }
	  ```
	* 개별 채팅방의 id값을 웹소켓 주소에 할당하여 채팅방마다 다른 웹소켓에 연결시켰습니다
	  ```js
	  chatSocket = new WebSocket(`${webSocketBaseUrl}/chats/${roomId}`)
	  ```
</details>
<br>

### 6-2. 데이터베이스 다수 조건 쿼리와 정렬 문제
<details markdown="1">
 <summary>자세한 내용 보기</summary>
  <br>
  
  * 문제 : 
  	* 알림 기능 구현에서 채팅 메시지를 종류에 따라 구분하여 데이터 처리해야했습니다
  	* 구분되어 처리된 데이터를 다시 합치고 시간 순으로 정렬을 해야했습니다
  	* 개발 버전과 배포 버전이 같은 코드임에도 정렬 순서가 다르고 매번 순서가 뒤죽박죽 바뀌는 문제가 발생했습니다
  * 해결 : 
  	* 채팅 메시지에 신청 메시지인지 아닌지 구분해주는 'application' boolean 필드를 추가해서 해당 필드로 조회했습니다
	* 구분된 메시지들을 원하는 구조에 맞게 데이터 처리 후 리스트에 append()로 다시 통합했습니다
	```py
	unread_message_list = []
	    for joined_chatroom in joined_chatrooms:
		# 읽지않은 채팅
		latest_unread_chat = joined_chatroom.chatmessage_set.filter(
		    is_read=False, application=False).exclude(user=user_id)
		if latest_unread_chat.exists():
		    latest_unread_chat = latest_unread_chat.last()
		    latest_unread_chat = {
			'room_id': joined_chatroom.id,
			'title': joined_chatroom.item.title,
			'sender': latest_unread_chat.user.nickname,
			'created_at': latest_unread_chat.created_at,
			'status': None,
		    }
		    unread_message_list.append(latest_unread_chat)
		# 읽지않은 거래상태
		latest_unread_contract = joined_chatroom.chatmessage_set.filter(
		    is_read=False, application=True).exclude(user=user_id)
		if latest_unread_contract.exists():
		    latest_unread_contract = latest_unread_contract.last()
		    latest_unread_contract = {
			'room_id': joined_chatroom.id,
			'title': joined_chatroom.item.title,
			'sender': latest_unread_contract.user.nickname,
			'created_at': latest_unread_contract.created_at,
			'contract_type': latest_unread_contract.contract_type,
		    }
		    unread_message_list.append(latest_unread_contract)
	```
	* 개발 버전에서는 따로 정렬에 대한 정의를 해주지않아도 기본값이 id 순으로 나오고 그게 곧 시간 순서라서 문제가 없었습니다<br>
	  그런데 배포 버전에서는 매 실행마다 조회한 쿼리셋의 정렬 순서가 랜덤으로 정렬되어있었습니다
	* 문제에 대한 해결은 append 한 리스트를 시간 순으로 정렬하는 것으로 굉장히 간단하게 해결이 가능하였지만
	  ```py
	  unread_message_list.sort(key=lambda x: x['created_at'])
	  ```
	* 도대체 왜? 개발 때와 배포가 같은 코드인데도 다른 결과가 나오는지 원인에 대한 호기심이 생겼습니다
	* 오랜 시간 팀원과 함께 원인 탐색을 한 뒤 개발, 배포 버전이 서로 다른 DB를 사용하고 있고<br>
	  DB 마다 필터링시 정렬을 지정해주지않으면 디폴트로 다른 기준을 갖고 정렬하여 보여준다는 것을 알았습니다
	* 각각 DB의 공식 문서에 따르면 필터링 시 개발 버전에 사용한 MySQL, SQLite 는 id 순으로 필터링하며,<br>
	  배포 버전에 사용한 PostgreSQL 에서는 랜덤 순으로 필터링 된다는 것을 알게됨으로써 원인도 파악하였습니다
</details>
<br>

## 7. 후기
https://velog.io/@wkdudhksl/이거대여-후기
