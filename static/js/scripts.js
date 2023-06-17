
// Mock python dictionary converted to a JS object
document.addEventListener("DOMContentLoaded", function() {
  const stream_commands = {
      "/stream time_and_sales": "Returns real-time time and sales data for 100 ticks.",
      "/stream double_quote": "Choose two stocks and stream their price in real-time for 200 ticks.",
      "/stream quote": "Choose a stock and stream its price in real-time for 200 ticks.",
      "/stream double_crypto": "Choose two crypto coins and stream their price in real-time for 200 ticks.",
      "/stream crypto": "Choose a crypto coin and stream its price in real-time for 200 ticks.",
      "/stream topvolume": "Find the top option for volume in real time.",
      "/stream tits": "Does exactly what it says..."
  };
  
  const commandContainer = document.createElement('div');
  
  for (const command in stream_commands) {
      const commandButton = document.createElement('button');
      commandButton.innerText = command;
      commandButton.classList.add('command-btn');
      commandButton.onclick = () => {
          const modalText = document.getElementById('modal-text');
          modalText.innerText = stream_commands[command];
          const modal = document.getElementById('myModal');
          modal.style.display = "block";
      };

      const commandBlock = document.createElement('div');
      commandBlock.classList.add('command-block');
      commandBlock.appendChild(commandButton);

      commandContainer.appendChild(commandBlock);
  }

  document.getElementById('app').appendChild(commandContainer);

  // Get the <span> element that closes the modal
  const span = document.getElementsByClassName("close")[0];

  // When the user clicks on <span> (x), close the modal
  span.onclick = function() {
    const modal = document.getElementById('myModal');
    modal.style.display = "none";
  }
});