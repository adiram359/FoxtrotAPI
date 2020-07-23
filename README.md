# FoxtrotAPI
The FoxtrotAPI allows you to fetch hilarious comic strips from the Foxtrot series by Bill Amend
### Usage
The FoxtrotAPI supports 1 ways of fetching a strip:

#### fetch(https://.../random)
This will allow you to fetch a random strip from a database of 400+ comic strips:
```javascript
var result = await(fetch("http://../random");
var comic_data = await result.json();
/* comic_data will be a JSON with the following data:
   {
      "_id": 2,
      "author": "Bill Amend",
      "title": "Iguanoman",
      "img_src": "http://1a3k5t1s1nlq3nug3z23q9ed-wpengine.netdna-ssl.com/wp-content/uploads/2020/07/ft200712-foxtrot-comics-bill-amend-iguanoman-2020-quincy-jason-          aliens-sunday-comic-strip.png"
    }
*/

```
