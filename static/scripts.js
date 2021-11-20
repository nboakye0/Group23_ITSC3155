document.addEventListener("DOMContentLoaded", function() {
    const path = window.location.pathname;
    const pathArray = path.split("/");
    const btn = document.getElementById("upvote");
    btn.addEventListener('click', () => {
        upvote = document.getElementById('votesup');
        const response = fetch(`http://127.0.0.1:5000/questions/${pathArray[2]}/upvote`, {
            method: 'POST'
        })
        let count = parseInt(upvote.innerHTML);
        count++;
        upvote.innerHTML = count;
        btn.disabled = true;
    });


    const downbtn = document.getElementById("downvote");
    downbtn.addEventListener('click', () => {
        let downvote = document.getElementById('votesup');
        const response = fetch(`http://127.0.0.1:5000/questions/${pathArray[2]}/downvote`, {
            method: 'POST'
        })
        let count = parseInt(downvote.innerHTML);
        count--;
        downvote.innerHTML = count;
        downbtn.disabled = true;
    });
});

