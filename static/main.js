const button = document.getElementById("fetchComic");
button.onclick = get_comic;

async function get_comic() {
  console.log("pressed")
  const x = await fetch("http://127.0.0.1:5000/random");
  const y = await x.json();
  console.log(y);

  const img = document.getElementById("comic");
  const img_title = document.getElementById("comicTitle");
  img.src = y.img_src;
  img_title.innerHTML = "'"+ y.title +"'" +" by Bill Amend";
}
get_comic()
