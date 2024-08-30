import express from 'express';
import http from 'http';
import { Server } from 'socket.io';

const app = express();
const server = http.createServer(app);
const io = new Server(server);

// Serve static files for the client
app.use(express.static('public'));

// Game state
let players = {};
let gameState = Array(9).fill(null);
let currentPlayer = 'X';
let gameActive = true;

// Winning combinations
const winningCombinations = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6],
];

io.on('connection', (socket) => {
    console.log('New player connected:', socket.id);

    // Assign the player to either X or O
    if (!players['X']) {
        players['X'] = socket.id;
        socket.emit('playerType', 'X');
    } else if (!players['O']) {
        players['O'] = socket.id;
        socket.emit('playerType', 'O');
    } else {
        socket.emit('message', 'Game is full');
        return;
    }

    // Start the game
    const playersArray = Object.keys(players);
    const randomIndex = Math.floor(Math.random() * playersArray.length);
    currentPlayer = playersArray[randomIndex];
    io.emit('gameUpdate', { gameState, currentPlayer });
    io.emit('turn', currentPlayer);

    // Handle player's move
    socket.on('makeMove', (index) => {
        if (gameActive && players[currentPlayer] === socket.id && gameState[index] === null) {
            gameState[index] = currentPlayer;
            io.emit('gameUpdate', { gameState, currentPlayer });
            io.emit('cellFilled', index); // Emit cellFilled event with the filled index
            const nextPlayer = currentPlayer === 'X' ? 'O' : 'X';
            io.emit('turn', nextPlayer); // Emit turn event
            if (checkWinner()) {
                io.emit('gameOver', { winner: currentPlayer });
                gameActive = false;
            } else if (gameState.every(cell => cell !== null)) {
                io.emit('gameOver', { winner: null }); // Game is a draw
                gameActive = false;
            } else {
                currentPlayer = currentPlayer === 'X' ? 'O' : 'X';
            }
        }
    });


    // Handle player disconnect
    socket.on('disconnect', () => {
        console.log('Player disconnected:', socket.id);
        if (players['X'] === socket.id) {
            delete players['X'];
        } else if (players['O'] === socket.id) {
            delete players['O'];
        }
        io.emit('resetGame');
        resetGame();
    });

    socket.on('restartGame', () => {
        resetGame();
    });
});

server.listen(3000, () => {
    console.log('Server is running on http://localhost:3000');
});

// Check if the current player has won the game
function checkWinner() {
    return winningCombinations.some(combination => {
        const [a, b, c] = combination;
        return gameState[a] === currentPlayer && gameState[a] === gameState[b] && gameState[a] === gameState[c];
    });
}

// Reset the game state for a new game
function resetGame() {
    gameState = Array(9).fill(null);
    currentPlayer = 'X';
    gameActive = true;
    io.emit('gameUpdate', { gameState, currentPlayer });
}

