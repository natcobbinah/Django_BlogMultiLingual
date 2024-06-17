let language_switcher = document.querySelector("#language-select")

language_switcher.onchange = (e) => {
    //console.log(e.target.value, e.target.options[e.target.selectedIndex].label)
    if (e.target.value === 'fr') {
        host_url = window.location.hostname
        pathname = '/fr/'
        window.history.replaceState({}, '', `${pathname}`)
    } else if (e.target.value === 'en') {
        host_url = window.location.hostname
        pathname = '/en/'
        window.history.replaceState({}, '', `${pathname}`)
    }
}

