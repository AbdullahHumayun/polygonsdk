let snippetCodeInterval;

function animateCodeTyping(element, code) {
    let i = 0;
    snippetCodeInterval = setInterval(() => {
        element.innerHTML += code.charAt(i);
        i++;
        if (i === code.length) {
            clearInterval(snippetCodeInterval);
        }
    }, 15);
}

function copyCodeSnippet() {
    const snippetCode = document.getElementById("snippet-code");
    const code = snippetCode.innerText;

    navigator.clipboard.writeText(code)
        .then(() => {
            console.log("Code snippet copied to clipboard!");
            const copyButton = document.getElementById("copy-button");
            copyButton.textContent = "Copied!";
            setTimeout(() => {
                copyButton.textContent = "Copy";
            }, 2000); // Change the delay (in milliseconds) as needed
        })
        .catch((error) => {
            console.error("Failed to copy code snippet:", error);
        });
}

let snippets = {};

function displayCodeSnippet() {
    const snippetSelect = document.getElementById("snippet-select");
    const snippetCode = document.getElementById("snippet-code");
    const selectedSnippet = snippetSelect.options[snippetSelect.selectedIndex].text;

    if (selectedSnippet === "") {
        snippetCode.innerText = "";
    } else {
        let snippet = "";

        if (window.snippets && window.snippets.polygonSnippets && window.snippets.polygonSnippets.hasOwnProperty(selectedSnippet)) {
            snippet = window.snippets.polygonSnippets[selectedSnippet];
        } else if (window.snippets && window.snippets.discordSnippets && window.snippets.discordSnippets.hasOwnProperty(selectedSnippet)) {
            snippet = window.snippets.discordSnippets[selectedSnippet];
        } else if (window.snippets && window.snippets.webullSnippets && window.snippets.webullSnippets.hasOwnProperty(selectedSnippet)) {
            snippet = window.snippets.webullSnippets[selectedSnippet];
        }
        else if (window.snippets && window.snippets.StockMarketHelperFunctions && window.snippets.StockMarketHelperFunctions.hasOwnProperty(selectedSnippet)) {
            snippet = window.snippets.StockMarketHelperFunctions[selectedSnippet];
        }

        else if (window.snippets && window.snippets.generalHelperFunctions && window.snippets.generalHelperFunctions.hasOwnProperty(selectedSnippet)) {
            snippet = window.snippets.generalHelperFunctions[selectedSnippet];
        }


        if (snippet) {
            clearInterval(snippetCodeInterval);
            snippetCode.innerText = "";
            animateCodeTyping(snippetCode, snippet);
        }
    }
}

function filterSnippetsByCategory() {
    const categorySelect = document.getElementById('category-select');
    const snippetSelect = document.getElementById('snippet-select');
    const selectedCategory = categorySelect.value;

    // Clear snippet dropdown
    snippetSelect.innerHTML = '';

    if (selectedCategory === '') {
        // If no category is selected, show default option
        const defaultOption = document.createElement('option');
        defaultOption.value = '';
        defaultOption.text = 'Select a snippet...';
        snippetSelect.appendChild(defaultOption);
    } else {
        // Get snippets for the selected category
        const categorySnippets = (window.snippets[selectedCategory] || {});
        if (categorySnippets) {
            // Create placeholder option for selected category
            const placeholderOption = document.createElement('option');
            placeholderOption.value = '';
            placeholderOption.text = `Pick a snippet...`;
            placeholderOption.disabled = true;
            placeholderOption.selected = true;
            snippetSelect.appendChild(placeholderOption);

            // Populate snippet dropdown with options
            for (const snippetName of Object.keys(categorySnippets)) {
                const option = document.createElement('option');
                option.value = snippetName;
                option.text = snippetName;
                snippetSelect.appendChild(option);
            }
        } else {
            // If no snippets are available for the selected category, show a message
            const noSnippetsOption = document.createElement('option');
            noSnippetsOption.value = '';
            noSnippetsOption.text = 'No snippets available';
            snippetSelect.appendChild(noSnippetsOption);
        }
    }
}