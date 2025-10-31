CREATE TABLE IF NOT EXISTS auditoria_interacoes (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    modulo VARCHAR(50),
    input_usuario TEXT,
    resultado TEXT
);
