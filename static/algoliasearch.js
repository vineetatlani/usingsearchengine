
const search = instantsearch({
    appId: "FOL57BHXOW",
    apiKey: "8ec1d2c0541c39a6879c59c2f79c4157",
    indexName: "dev_MYBLOG",
    routing: true
  });

search.addWidgets([
  instantsearch.widgets.searchBox({
    container: '#searchbox'
  }),

  instantsearch.widgets.hits({
    container: '#hits'
    // templates: {
    //     empty: "No results.",
    //     item: function(hit) {
    //       return hitTemplate(hit);
    //     }
    //   }
  })
]);

search.start();

// function hitTemplate(hit) {
//     return `
//       <div class="hit">
//             <div class="hit-name">${hit._highlightResult.title.value}</div>
//             </div>
//       </div>
//     `;
//   }