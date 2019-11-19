# Vue test 정리

1. Vue.js에 대한 설명 중 옳지 않은 것은?

   답 : vue CLI를 사용해야지만 Vue 개발이 가능하다.

2. 디렉티브 중 HTML 요소의 속성을 다룰 때 사용하는 것을 고르시오

   답: v-bind

3. Vue 인스턴스를 초기화 하는 객체(Object) 속성들 중에서 컴포넌트의 이름을 의미하는 것을 고르시오.

   답: name

4. v-on 디렉티브의 줄임 표현으로 옳은 것을 고르시오.

   답: @

5. Vue 인스턴스를 초기화 하는 객체(Object) 속성들 중에서, 화면에 표시할 요소들(HTML)을 정의하는 것을 고르시오.

   답 : template

6. Vue.js가 import 되어 있고 지문의 코드가 body 태그 내에 작성된 html 파일이 있다.  Vue 인스턴스의 data 속성인 imageUrl에 저장된 URL을 사용해 브라우저에 이미지를 보여주려고 할 때, 빈칸 (a)에 들어갈 코드로 옳은 것을 고르시오.

   답: <img v-bind:src="imageurl">

7. Vue.js가 import되어있고 지문의 코드가 body태그내에 작성된 html 파일이 있다. 결과가 다른 하나를 고르시오.

   답: watch가 들어간 것!

8. 지문의 코드는 동영상을 출력할 VideoDetail 컴포넌트이다. computed 속성의 videoURL의 함수를 화살표함수로 바꿨을 때 문제로 옳은 것을 고르시오.

   답: this.video.id 가 문제

9. 지문은 영화정보를 보여주기 위한 App.vue 파일이다. 설명으로 옳은 것은?

   답: props속성에 Movies와 Genres를 추가해야 한다.

10. 컴포넌트에 대한 설명으로 옳은 것을 고르시오.

    답: 부모 컴포넌트 데이터가 업데이트되면 자식도 자동 갱신

11. 다음 보기들 중, Vue.js의 데이터 바인딩에서 사용 가능한 JS표현식으로 옳지 않은 것을 고르시오.

    답:{{const number = 1}}

12. 디렉티브 v-if 와 v-show의 차이점은?

    답: v-if는 조건문을 만족할 경우만 렌더링 v-show는 상관없이 렌더링

13. vue인스턴스와 연결된 element에 접근하기 위한 JS표현식으로 적합한것은?

    답: $el.app

14. 지문의 코드에서 ChildComponent가 받아보게 되는 props의 이름을 고르시오.

    답: d

15. 부모 컴포넌트로 올라가는?

답: videoSelect

16. App.vue 컴포넌트파일, 데이터속성이 올바르게 동작 빈칸 (a)?

    답: data(){

{}

}

17. vue-cli를 통해 프로젝트를 구성한 것, 옳지 않은 것은?

    답: App.vue 컴포넌트는 root 인스턴스와 형제 관계이다.

18.  Vue.js가 임포트 되어있고 %3은 3으로 나눴을 때 나머지가 1이상인 수

    답: 124578

19. 뷰클리로 투두 프로젝트 올바르게 짝지어진것은?

    template을 묶지 않았다.

20. 양방향 바인딩은?

답: v-model

21. .innerHTML

    답: V-html

22. 축약하기 v-bind

23. 빈칸 (a) 들어갈 코드 답:click

24. Welcome to the Vue world!

    답: post.content



