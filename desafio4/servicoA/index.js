const express = require('express');
const app = express();
const PORT = 3000;

const users = [
    { id: 1, name: "Alice Tech", joined_at: "2023-01-15" },
    { id: 2, name: "Bob Docker", joined_at: "2023-03-10" },
    { id: 3, name: "Charlie Cloud", joined_at: "2023-05-22" }
];

app.get('/api/users', (req, res) => {
    console.log("Recebida requisição para listar usuários");
    res.json(users);
});

app.listen(PORT, () => {
    console.log(`Service A rodando na porta ${PORT}`);
});