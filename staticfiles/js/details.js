
function toggleComments(){
  let comments = document.getElementById('comments-box')

  if(comments.style.color = 'none'){
    comments.style.display = 'flex'
  } else{
    comments.style.display = 'none'
  }
}