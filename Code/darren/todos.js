var app = new Vue({
    el: '#app',
    data: {
        message: 'todos:',
        todos: [
          {'todo': 'Learn Vue.js', 'completed': false},
          {'todo': 'Master frontend', 'completed': false}
        ],
        todo: '',
    },
    methods: {
        addTodo: function(event) {
          console.log(event)
          entry = {'todo': `${event.target.value}`, 'completed': false}
          app.todos.push(entry)
        },
        removeTodo: function(index) {
          app.todos.pop(index)
        },
        markDone: function(index) {
          app.todos[index]['completed'] = true
        },
    },
});
