

// Handle connection event
socket.on("connect", () => {
	console.log("Connected to server");
});

// Handle incoming messages from the server
socket.on("message", (data) => {
	console.log("Message from server:", data);
});

// Handle game state updates from the server
socket.on("gameState", (data) => {
	updateBoard(data.board);
	char = data.nextChar;
});

// Send a message to the server
socket.send("Hello from the client!");

// Handle disconnection event
socket.on("disconnect", () => {
	console.log("Disconnected from server");
});

let char = 'X';
const box = document.getElementById("box");
const board = Array(9).fill(null);

box.onclick = (e) => {
	if (e.target.innerText || !socket.connected) return;
	board[e.target.id] = e.target.innerText = char;
	char = char === 'X' ? 'O' : 'X';
	const winner = calculateWinner(board);
	if (winner) {
		box.innerHTML = `<div>gg</div><div>Winner is ${winner}</div><div>ez</div>`;
	} else if (board.find((v) => v == null) === undefined) {
		box.innerHTML = "DRAW";
	}
	socket.emit("gameState", { board, nextChar: char });
};

function updateBoard(newBoard) {
	for (let i = 0; i < newBoard.length; i++) {
		document.getElementById(i).innerText = newBoard[i];
	}
}

function calculateWinner(squares) {
	const lines = [
		[0, 1, 2],
		[3, 4, 5],
		[6, 7, 8],
		[0, 3, 6],
		[1, 4, 7],
		[2, 5, 8],
		[0, 4, 8],
		[2, 4, 6],
	];
	for (let i = 0; i < lines.length; i++) {
		const [a, b, c] = lines[i];
		if (squares[a] && squares[a] === squares[b] && squares[a] === squares[c]) {
			return squares[a];
		}
	}
	return null;
}