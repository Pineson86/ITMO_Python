#Описание

*Сервер запускается по адресу: (http://127.0.0.1:5000/add ).
*Сервер выполняет функцию сложения переданных ему при post-запросе. 
*Пример команды для Windows PowerShell, которая отпарвляет http-post-запрос на сервер с параметрамиa=3, b= 6.
Invoke-RestMethod -Uri http://127.0.0.1:5000/add -Method Post -ContentType "application/json" -Body '{"a": 3, "b": 6}'
