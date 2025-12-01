const express = require('express');
const app = express();
const PORT = 3000;

app.get('/', (req, res) => {
    res.json({
        service: "Users Service",
        data: [
            { id: 1, name: "João Silva", email: "joao@email.com" },
            { id: 2, name: "Maria Oliveira", email: "maria@email.com" }
        ]
    });
});

app.listen(PORT, () => console.log(`Users Service running on port ${PORT}`));