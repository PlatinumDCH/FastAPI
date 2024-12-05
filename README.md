краткое описание 
чем можно заменить авторизвцию?
    https://www.keycloak.org/
    https://aws.amazon.com/ru/cognito/
    через github \
    через google  \ в данном случаем просто скидываем auth на сторонние сервисы

авторицация
jwt - json web token
https://jwt.io/
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
этот токен из 3 частей XXX.YYY.ZZZ
1 часть herader - содержит информацию, которая определяет алгоритм хеширования
{
  "alg": "HS256",
  "typ": "JWT"
}
2 часть pyload - эта часть и информацией которую нужно послать при помощи токена. Он не защищен и может шифроваться без скретнго ключа- 
это обычная кодировка Base64. Токе не предназначен для ширования конфиденциальной иноформации(пароли, ... )
{
  "sub": "1234567890",
  "name": "John Doe",
  "iat": 1516239022
}
3 часть это signature - соединяет закодированй herader pyload с секретным ключом и надежно кодирует с 
использрвание алгоритма хеширования
