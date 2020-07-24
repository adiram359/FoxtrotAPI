# FoxtrotAPI
The FoxtrotAPI allows you to fetch hilarious comic strips from the Foxtrot series by Bill Amend
### Usage
The FoxtrotAPI supports 2 ways of fetching a strip from a database of 400+ comic strips:

### 1. Fetching a random comic strip:
   ```javascript
   var result = await fetch("http://../random");
   var comic_data = await result.json();
   /* comic_data will be a JSON with the following data:
      {
         "_id": 2,
         "author": "Bill Amend",
         "title": "Iguanoman",
         "img_src": "http://1a3k5t1s1nlq3nug3z23q9ed-wpengine.netdna-ssl.com/wp-content/uploads/2020/07/ft200712-foxtrot-comics-bill-amend-iguanoman-2020-quincyjason-aliens-sunday-comic-strip.png"
       }
   */
   ```

### 2. Fetching a strip by title:
   ```javascript
   var result = await fetch("https://.../title=<strip_title>);
   //replace <strip_title> with the title of the comic strip you want to fetch, such as Iguanoman.
   ```

### 3. Fetch a strip by the date it was published:
  ```javascript
  var result = await fetch("https://foxtrot.io/date/Month.Date.Year");
  //replace Month.Date.Year i.e 01.16.1960 for January 16th, 1960
  ```


Here's the strip fetched above: "Iguanoman" by Bill Amend.
![Here's the strip fetched above](http://1a3k5t1s1nlq3nug3z23q9ed-wpengine.netdna-ssl.com/wp-content/uploads/2020/07/ft200712-foxtrot-comics-bill-amend-iguanoman-2020-quincy-jason-aliens-sunday-comic-strip.png)
