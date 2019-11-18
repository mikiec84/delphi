function makeTippy(node) {
    return tippy(node.popperRef(), {
        html: (function(){
            var div = document.createElement('div');
            div.innerHTML = node.data('tooltip');
            return div;
        })(),
        trigger: 'manual',
        placement: 'bottom',
        arrow: true,
        hideOnClick: 'toggle',
        multiple: true,
        sticky: true,
        interactive: true,
        theme: 'light',
    }).tooltips[0];
}

function toggle_tooltip(event) {
  var node = event.target;
  node.deselect();
  node.toggleClass('selectedNode');
}

// This function creates the cytoscape graph objects
function make_cyto_viewer(pane_id, nodesAndEdges){
  var G = cytoscape({
    container: $(pane_id),
    elements: nodesAndEdges,
    maxZoom : 2,
    minZoom : 0.1,
    selectionType: 'additive',
    layout: {
      fit: true,
      name: 'dagre',
      rankDir: 'LR',
      nodeDimensionsIncludeLabels: true,
      spacingFactor: 0.8,
    },
    style: [
      {
        selector: 'node',
        style: {
          'label': 'data(label)',
          'shape': 'data(shape)',
          'background-color': 'white',
          'border-color': 'data(color)',
          'border-width': '3pt',
          'font-family': 'Menlo, PT Sans, sans-serif',
          'width': 'label',
          'height': 'data(height)',
          'text-valign': 'data(textValign)',
          'padding': 'data(padding)',
        }
      }, {
        selector: 'edge',
        style: {
          'curve-style' : 'bezier',
          'target-arrow-shape': 'triangle',
        }
      }, {
        selector: '.selectedNode',
        style: {
          'background-color': '#d3d3d3',
        }
      }
    ]
  });
  // G.nodes().forEach(function(ele){
  //     ele.scratch()._tippy = makeTippy(ele);
  // });

  G.on('tap', 'node', function(evt){
    var node = evt.target;
      if (!node.selected()){
        if (!node.hasClass('cy-expand-collapse-collapsed-node') && !node.isParent()) {
          node.scratch()._tippy.show();
          MathJax.Hub.Queue(["Typeset", MathJax.Hub]);
        }
      }
      else {
        node.scratch()._tippy.hide();
      }
      node.toggleClass('selectedNode');
  });

  // add the panzoom control
  G.panzoom({
    zoomFactor: 0.05, // zoom factor per zoom tick
    zoomDelay: 45, // how many ms between zoom ticks
    minZoom: 0.1, // min zoom level
    maxZoom: 10, // max zoom level
    fitPadding: 50, // padding when fitting
    panSpeed: 10, // how many ms in between pan ticks
    panDistance: 10, // max pan distance per tick
    panDragAreaSize: 75, // length of the pan drag box in which the vector for panning is calculated (bigger = finer control of pan speed and direction)
    panMinPercentSpeed: 0.25, // slowest speed to pan (as a percent of panSpeed)
    panInactiveArea: 8, // radius of inactive area in pan drag box
    panIndicatorMinOpacity: 0.5, // min opacity of pan indicator (the draggable nib); scales from this to 1.0
    zoomOnly: false, // minimal version of the ui only with zooming (useful on systems with bad mousewheel resolution)
    fitSelector: undefined, // selector of elements to fit
    animateOnFit: () => { return false; }, // whether to animate on fit
    fitAnimationDuration: 1000, // duration of animation on fit
    // icon class names
    sliderHandleIcon: 'fa fa-minus',
    zoomInIcon: 'fa fa-plus',
    zoomOutIcon: 'fa fa-minus',
    resetIcon: 'fa fa-expand'
  });

  G.expandCollapse({fisheye: false, undoable: false});
  G.nodes().on("expandcollapse.afterexpand", toggle_tooltip);
  G.nodes().on("expandcollapse.aftercollapse", toggle_tooltip);
  return G;
}

// ====================================
// Computational Graph
// ====================================

// var computational_graph = make_cyjs(
//   'computational_graph',
//   {{ scopeTree_elementsJSON | safe }}
// );



// ====================================
// Causal Analysis Graph
// ====================================

// var causal_analysis_graph = make_cyjs(
//   'causal_analysis_graph',
//   {{ program_analysis_graph_elementsJSON | safe }}
// );
// causal_analysis_graph.fit();
// causal_analysis_graph.pan({x:70,y:70});

// ====================================
// Forward Influence Blanket
// ====================================
// var forward_influence_blanket = make_cyjs(
//   'fib',
//   {{ fib_elementsJSON | safe }}
// );
