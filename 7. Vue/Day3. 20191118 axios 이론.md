# 2019. 11. 18 Vue.JS Axios

클라이언트(HTML) - 서버(Django)

1. 로그인 
2. 유저확인
3. 확인 완료
4. 세션 생성 -> JWT 발급
5. 세션발급
6. 응답 ( + Session ID)
7. 데이터 요청 (CRUD) + Session ID
8. 쿠키 검증
9. 유저정보 확인
10. 응답



클라이언트(Vue) - 서버(Django)

1. 로그인 
2. 유저확인
3. 확인 완료
4.  JWT 발급
5. 응답 ( + JWT)
6. 데이터 요청 (CRUD) + JWT
7. JWT 검증
8. 응답



##### 라우터 생성

[Home](http://localhost:8080/) | [About](http://localhost:8080/about)

![Vue logo](http://localhost:8080/img/logo.82b9c7a5.png)

# Welcome to Your Vue.js App

For a guide and recipes on how to configure / customize this project,
check out the [vue-cli documentation](https://cli.vuejs.org/).

### Installed CLI Plugins

- [babel](https://github.com/vuejs/vue-cli/tree/dev/packages/%40vue/cli-plugin-babel)
- [eslint](https://github.com/vuejs/vue-cli/tree/dev/packages/%40vue/cli-plugin-eslint)

### Essential Links

- [Core Docs](https://vuejs.org/)
- [Forum](https://forum.vuejs.org/)
- [Community Chat](https://chat.vuejs.org/)
- [Twitter](https://twitter.com/vuejs)
- [News](https://news.vuejs.org/)

### Ecosystem

- [vue-router](https://router.vuejs.org/)
- [vuex](https://vuex.vuejs.org/)
- [vue-devtools](https://github.com/vuejs/vue-devtools#vue-devtools)
- [vue-loader](https://vue-loader.vuejs.org/)
- [awesome-vue](https://github.com/vuejs/awesome-vue)



VUE = 싱글페이지어플리케이션을 만들기 위한 라이브러리

VUE CLI => 뷰의 기본구조 잡아주는 것