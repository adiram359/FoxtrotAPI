# FoxtrotAPI
```
async function get_comic() {
  const x = await fetch("http://127.0.0.1:5000/random");
  const y = await x.json();
  console.log(y);

  const img = document.getElementById("comic");
  img.src = y.img_src;
}
get_comic() 

```
