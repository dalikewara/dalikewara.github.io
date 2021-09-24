document$.subscribe(() => {
  hljs.highlightAll()
  let tables = document.querySelectorAll("article table")
  tables.forEach(function(table) {
    new Tablesort(table)
  })
})