function onload() {
    console.log("No")
}

function apply_hover() {
    const linkBox = document.getElementById("fileLink")
    const linkBoxHover = document.getElementById("fileLinkHover")
    linkBox.addEventListener('mouseover', function (event) {
        const element = document.getElementById(event.target.id)
        element.classList.add('cAnimate')


        // const element = document.getElementById("line")
        // element.style.animation = "none"
        // element.style.animation = "link_animation 2s linear"
        // console.log("here")

        // let id = null
        // const elem = document.getElementById("line")
        // let pos = linkBox.getBoundingClientRect().top
        // clearInterval(id)
        // id = setInterval(frame, 1)
        // function frame() {
        //     if (pos == 270) {
        //         clearInterval(id)
        //     } else {
        //         pos++
        //         elem.style.top = pos + "px";

        //     }
        // }

        // const currElement = document.getElementById("fileLinkHover")
        // currElement.classList.remove("hidden")
        // currElement.classList.add("file_link")
        // linkBox.classList.remove("file_link")
        // linkBox.classList.add("hidden")
    })
    linkBox.addEventListener('mouseout', function (event) {
        const element = document.getElementById(event.target.id)
        element.classList.remove('cAnimate')
    })


    // linkBoxHover.addEventListener('mouseout', function (event) {
    //     const currElement = document.getElementById("fileLink")
    //     currElement.classList.remove("hidden")
    //     currElement.classList.add("file_link")

    //     linkBoxHover.classList.remove("file_link")
    //     linkBoxHover.classList.add("hidden")
    // })
}