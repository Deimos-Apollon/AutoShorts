# AutoShorts

Для работы необходим файл TOKENS.py с данными токенов различных API.

Генерация видео происходит в файле `src/video_creation/create_content_video.py`, подробности в 
`src/video_creation/README.md`.

# Зависимости
При установке зависимостей может понадобиться создание новых переменных окружения (в Windows точно).
1. eSpeak
2. ImageMagick
3. ffmpeg


# Генерация
В папку `input` переносятся все медиафайлы - видео, музыка, текст, озвученный текст.

Озвученный текст получается из `src/text_to_voice`. Здесь можно настроить параметры голоса. При выполнении
озвучки рекомендуется сохранять результат в `input/voiced/`. Такой путь по умолчанию настроен в скрипте `voice_text.py`.

Сама компоновка видео, аудио и субтитров происходит в `src/video_creation/create_content_video.py`. На выходе получается
сгенерированный шортс в папке `output`.
