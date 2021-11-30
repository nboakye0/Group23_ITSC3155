document.addEventListener("DOMContentLoaded", function() {
    const path = window.location.pathname;
    const pathArray = path.split("/");
    const btn = document.getElementById("upvote");
    const downbtn = document.getElementById("downvote");
    let upClicked = false;
    let downClicked = false;
    btn.addEventListener('click', () => {
        if (upClicked == false && downClicked == false) {
            upvote = document.getElementById('votesup');
            const response = fetch(`http://127.0.0.1:5000/questions/${pathArray[2]}/upvote`, {
                method: 'POST'
            })
            let count = parseInt(upvote.innerHTML);
            count++;
            upvote.innerHTML = count;
            upClicked = true;
        }
        else if (downClicked == true) {
            upvote = document.getElementById('votesup');
            const response = fetch(`http://127.0.0.1:5000/questions/${pathArray[2]}/upvote`, {
                method: 'POST'
            })
            let count = parseInt(upvote.innerHTML);
            count = count + 2;
            upvote.innerHTML = count;
            upClicked = true;
            downClicked = false;
        }
        else {
            let downvote = document.getElementById('votesup');
            const response = fetch(`http://127.0.0.1:5000/questions/${pathArray[2]}/downvote`, {
                method: 'POST'
            })
            let count = parseInt(downvote.innerHTML);
            count--;
            downvote.innerHTML = count;
            upClicked = false;
            downClicked = false;
        }
    });


    downbtn.addEventListener('click', () => {
        if (upClicked == false && downClicked == false) {
            let downvote = document.getElementById('votesup');
            const response = fetch(`http://127.0.0.1:5000/questions/${pathArray[2]}/downvote`, {
                method: 'POST'
            })
            let count = parseInt(downvote.innerHTML);
            count--;
            downvote.innerHTML = count;
            downClicked = true;
        }
        else if (upClicked == true) {
            downvote = document.getElementById('votesup');
            const response = fetch(`http://127.0.0.1:5000/questions/${pathArray[2]}/downvote`, {
                method: 'POST'
            })
            let count = parseInt(downvote.innerHTML);
            count = count - 2;
            downvote.innerHTML = count;
            upClicked = false;
            downClicked = true;
        }
        else {
            upvote = document.getElementById('votesup');
            const response = fetch(`http://127.0.0.1:5000/questions/${pathArray[2]}/upvote`, {
                method: 'POST'
            })
            let count = parseInt(upvote.innerHTML);
            count++;
            upvote.innerHTML = count;
            upClicked = false;
            downClicked = false;
        }
    });
});

