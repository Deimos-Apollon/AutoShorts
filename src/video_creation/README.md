Генерация видео происходит в файле `create_content_video.py`. Предварительно нужно преобразовать текстовую историю
в озвученную (см. README в `text_to_voice`).

Для генерации шортса нужно перейти в `create_content_video.py` и в нижней части поменять переменные
`video_filename, voiced_story_filename, music_filename, out_video_filename`.

Также, можно импортировать в свой скрипт функцию create_content_video и передать в неё соответствующие параметры.