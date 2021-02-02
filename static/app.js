const searchClient = algoliasearch('FOL57BHXOW', '8ec1d2c0541c39a6879c59c2f79c4157');

const search = instantsearch({
  indexName: 'demo_myblog',
  searchClient,
  routing: true
});

search.addWidgets([
  instantsearch.widgets.searchBox({
    container: '#searchbox',
    hitsPerPage: 5,
    placeholder: "Search by algolia"
  }),

  instantsearch.widgets.hits({
    container: '#hits',
    templates: {
        empty: "No results.",
        item: function(hit) {
          return `
          <div class="hit">
                <a href="#">${hit._highlightResult.title.value}</a><br>
                
                </div>
          </div>
        `;
        }
      }
  })
]);


search.start();