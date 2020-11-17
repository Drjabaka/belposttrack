Получение данных о посылке по треку с сайта belpost.by
```
import belpost
track = belpost.Track('track-name') 

# get last status
print(track.status())

# get all in text format
print(track.get_all())

# raw data
print(track.items)
```
