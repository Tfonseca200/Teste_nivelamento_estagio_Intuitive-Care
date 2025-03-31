<template>
  <div class="container">
    <h2>Buscar Empresas</h2>
    <div class="search-bar">
      <input v-model="termo" type="text" placeholder="Digite o nome" @keyup.enter="buscar" />
      <button @click="buscar">Buscar</button>
    </div>

    <div v-if="loading" class="loading">Carregando...</div>
    <div v-else-if="error" class="error">{{ error }}</div>
    
    <div v-else>
      <h3 v-if="resultados.length">Resultados:</h3>
      <div v-if="resultados.length" class="result-list">
        <div class="result-card" v-for="(empresa, index) in resultados" :key="index">
          <h4>{{ empresa.Nome_Fantasia }}</h4>
          <p><strong>Razão Social:</strong> {{ empresa.Razao_Social }}</p>
          <p v-for="(valor, chave) in empresa" :key="chave">
            <strong>{{ chave.replace('_', ' ') }}:</strong> {{ valor }}
          </p>
        </div>
      </div>
      <p v-if="!resultados.length">Nenhum resultado encontrado.</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      termo: "",
      resultados: [],
      loading: false,
      error: null
    };
  },
  methods: {
    async buscar() {
      if (!this.termo) return;
      this.loading = true;
      this.error = null;

      try {
        const response = await fetch(`http://127.0.0.1:8000/buscar?q=${encodeURIComponent(this.termo)}`);
        if (!response.ok) throw new Error("Erro ao buscar os dados");
        const data = await response.json();
        this.resultados = data.resultado || [];
      } catch (err) {
        this.error = err.message;
      } finally {
        this.loading = false;
      }
    }
  }
};
</script>

<style scoped>
.container {
  max-width: 800px;
  margin: auto;
  text-align: center;
  font-family: Arial, sans-serif;
}
.search-bar {
  display: flex;
  justify-content: center;
  margin-bottom: 15px;
}
input {
  padding: 10px;
  flex: 1;
  border: 1px solid #ccc;
  border-radius: 5px;
  margin-right: 5px;
}
button {
  padding: 10px;
  background: #007bff;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}
button:hover {
  background: #0056b3;
}
.loading {
  font-size: 16px;
  color: #666;
}
.error {
  color: red;
  margin-top: 10px;
}
.result-list {
  display: flex;
  flex-direction: column;
  gap: 10px;
}
.result-card {
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 5px;
  background: #f9f9f9;
  transition: 0.3s;
  text-align: left;
}
.result-card:hover {
  background: #e0e0e0;
}
h4 {
  margin: 0 0 5px;
  color: #333;
}
p {
  margin: 5px 0;
  color: #666;
}
</style>
