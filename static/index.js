
const sc_option1 = document.getElementById('sc_option1');
const sc_option4 = document.getElementById('sc_option4');
const terminal = document.getElementById('terminal');
const sc_option3 = document.getElementById('sc_option3');
const sc_option2 = document.getElementById('sc_option2');


/* Loop through the room json for each room and display it */
// If the show all rooms box is clicked do this
sc_option4.addEventListener('click', () => {
    terminal.innerHTML = '';
    let terminal_header = document.createElement('p');
    terminal_header.textContent = 'Here are all the rooms:';
    terminal_header.style.textAlign = 'center';
    terminal_header.style.fontSize = '40px';
    terminal.appendChild(terminal_header);
    fetch('http://localhost:8000/rooms')
        .then(response => response.json())
        .then(data => {
            let rooms = data.Rooms;
            rooms.forEach(room => {
                // Create a new paragraph for each room
                let paragraph = document.createElement('p');
                paragraph.textContent = room;
                paragraph.style.textAlign = 'center';
                paragraph.style.fontSize = '40px';

                // Append the paragraph to the "myElement" div
                terminal.appendChild(paragraph);
            });
        })
        .catch(error => {console.error('Error:', error);});
});

//if the delete a room is clicked do this
sc_option3.addEventListener('click', () => {
    terminal.innerHTML = '';
    let terminal_header = document.createElement('p');
    terminal_header.textContent = 'Here are all the current rooms:';
    terminal_header.style.textAlign = 'center';
    terminal_header.style.fontSize = '40px';
    terminal.appendChild(terminal_header);
    //Show the user all the rooms
    fetch('http://localhost:8000/rooms')
        .then(response => response.json())
        .then(data => {
            let rooms = data.Rooms;
            
            let paragraph = document.createElement('p');
            paragraph.textContent = rooms;
            paragraph.style.textAlign = 'center';
            paragraph.style.fontSize = '40px';
            terminal.appendChild(paragraph);

            let guide_paragraph = document.createElement('p');
            guide_paragraph.textContent = "Please enter the name of the room you want to delete:";
            guide_paragraph.style.textAlign = 'center';
            guide_paragraph.style.marginTop = '20px';
            guide_paragraph.style.fontSize = '40px';
            terminal.appendChild(guide_paragraph);

            // Create input box
            let inputBox = document.createElement('input');
            inputBox.type = 'text';
            inputBox.id = 'inputData';
            inputBox.name = 'inputData';
            terminal.appendChild(inputBox);

            // Create submit button
            let submit = document.createElement('button');
            submit.textContent = 'Submit';
            submit.addEventListener('click', function() {
                let t_inputData = document.getElementById('inputData').value;
                // Send the data to the server using the Fetch API
                fetch(`http://localhost:8000/delete-room/${t_inputData}`, {
                    method: 'DELETE'
                })
                .then(response => response.json())
                .then(data => {
                    console.log('Success:', data);
                })
                .catch((error) => {
                    console.error('Error:', error);
                });
            });
            terminal.appendChild(submit);
        })
        .catch(error => {console.error('Error:', error);});
        
});



//if the create a room is clicked do this
sc_option1.addEventListener('click', () => {
    terminal.innerHTML = '';
    let terminal_header = document.createElement('p');
    terminal_header.textContent = 'Here are all the current rooms:';
    terminal_header.style.textAlign = 'center';
    terminal_header.style.fontSize = '40px';
    terminal.appendChild(terminal_header);
    //Show the user all the rooms
    fetch('http://localhost:8000/rooms')
        .then(response => response.json())
        .then(data => {
            let rooms = data.Rooms;
            
            let paragraph = document.createElement('p');
            paragraph.textContent = rooms;
            paragraph.style.textAlign = 'center';
            paragraph.style.fontSize = '40px';
            terminal.appendChild(paragraph);

            let guide_paragraph = document.createElement('p');
            guide_paragraph.textContent = "Please enter the name of the room you want to create:"
            guide_paragraph.style.textAlign = 'center';
            guide_paragraph.style.marginTop = '20px';
            guide_paragraph.style.fontSize = '40px';
            terminal.appendChild(guide_paragraph);
            
            // Create input box
            let inputBox = document.createElement('input');
            inputBox.type = 'text';
            inputBox.id = 'inputData';
            inputBox.name = 'inputData';
            terminal.appendChild(inputBox);

            // Create submit button
            let submit = document.createElement('button');
            submit.textContent = 'Submit';
            submit.addEventListener('click', function() {
                let t_inputData = document.getElementById('inputData').value;
                // Send the data to the server using the Fetch API
                fetch(`http://localhost:8000/create-room/${t_inputData}`, {
                    method: 'POST'
                })
                .then(response => response.json())
                .then(data => {
                    console.log('Success:', data);
                })
                .catch((error) => {
                    console.error('Error:', error);
                });
            });
            terminal.appendChild(submit);
        })
        .catch(error => {console.error('Error:', error);});
        
});

//if the perform an operation button is clicked do this
sc_option2.addEventListener('click', () => {
    terminal.innerHTML = '';
    let terminal_header = document.createElement('p');
    terminal_header.textContent = 'Here are all the current rooms:';
    terminal_header.style.textAlign = 'center';
    terminal_header.style.fontSize = '40px';
    terminal.appendChild(terminal_header);
    //Show the user all the rooms
    fetch('http://localhost:8000/rooms')
        .then(response => response.json())
        .then(data => {
            let rooms = data.Rooms;
            
            let paragraph = document.createElement('p');
            paragraph.textContent = rooms;
            paragraph.style.textAlign = 'center';
            paragraph.style.fontSize = '40px';
            terminal.appendChild(paragraph);

            let guide_paragraph = document.createElement('p');
            guide_paragraph.textContent = "Please enter the name of the room you want to perform an operation on:";
            guide_paragraph.style.textAlign = 'center';
            guide_paragraph.style.marginTop = '20px';
            guide_paragraph.style.fontSize = '40px';
            terminal.appendChild(guide_paragraph);

            // Create input box
            let inputBox = document.createElement('input');
            inputBox.type = 'text';
            inputBox.id = 'inputData';
            inputBox.name = 'inputData';
            terminal.appendChild(inputBox);

            // Create submit button
            let submit = document.createElement('button');
            submit.textContent = 'Submit';
            submit.id = 'submitButton';
            submit.name = 'submitButton';
            submit.addEventListener('click', function() {
                let t_inputData = document.getElementById('inputData').value;
                location.href = `http://localhost:8000/operation-room/${t_inputData}`;
            });
            terminal.appendChild(submit);
        });
});



//we are going to send the user to a new html page that is filled with jinja html 
//ex. window.location.href = 'http://localhost:8000/get-jinja'; llok