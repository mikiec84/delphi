/*
#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "AnalysisGraph.hpp"
#include "doctest.h"
#include <fmt/core.h>

using namespace std;
string inflation = "wm/concept/causal_factor/economic_and_commerce/economic "
                   "activity/market/inflation";
string migration =
    "wm/concept/causal_factor/social_and_political/migration/human_migration";
string food_security = "wm/concept/causal_factor/condition/food_security";

vector<CausalFragment> causal_fragments = {
    {{"large", -1, inflation}, {"small", 1, migration}},
    {{"large", 1, migration}, {"small", -1, food_security}},
    {{"large", 1, migration}, {"small", -1, food_security}},
};

TEST_CASE("Testing model training") {
  RNG* R = RNG::rng();
  R->set_seed(87);

  AnalysisGraph G = AnalysisGraph::from_causal_fragments(causal_fragments);

  G.map_concepts_to_indicators();
  G.to_png();

  G[migration].replace_indicator(
      "Net migration", "New asylum seeking applicants", "UNHCR");

  G.construct_beta_pdfs();
  G.train_model(2015, 1, 2015, 12, 100, 900);

  Prediction preds = G.generate_prediction(2015, 1, 2015, 12);
  fmt::print("Prediction to array\n");

  try {
    vector<vector<double>> result =
        G.prediction_to_array("New asylum seeking applicants");
    fmt::print("Size of result is {} x {}\nFirst value of result is {}\n",
               result.size(),
               result[0].size(),
               result[0][0]);
  }
  catch (IndicatorNotFoundException& infe) {
    fmt::print(infe.what());
  }
}
*/

#include "AnalysisGraph.hpp"

using namespace std;


AnalysisGraph create_base_CAG(string uncharted_json_file) {
    AnalysisGraph G = AnalysisGraph::from_uncharted_json_file(uncharted_json_file);

    bool same_polarity = false;
    G.merge_nodes(
        "wm/concept/causal_factor/condition/food_security",
        "wm/concept/causal_factor/condition/food_insecurity",
        same_polarity
    );

    bool inward = true;
    G = G.get_subgraph_for_concept(
        "wm/concept/causal_factor/condition/food_insecurity", inward);

    G.map_concepts_to_indicators();
    return G;
}

void set_indicator(AnalysisGraph G, string concept, string indicator_new, string source) {
    G.delete_all_indicators(concept);
    G.set_indicator(concept, indicator_new, source);
}

void curate_indicators(AnalysisGraph G) {
    set_indicator(
        G,
        "wm/concept/indicator_and_reported_property/weather/rainfall",
        "Average Precipitation",
        "DSSAT"
    );

    set_indicator(
        G,
        "wm/concept/indicator_and_reported_property/agriculture/Crop_Production",
        "Average Harvested Weight at Maturity (Maize)",
        "DSSAT"
    );

    set_indicator(
        G,
        "wm/concept/causal_factor/condition/food_insecurity",
        "IPC Phase Classification",
        "FEWSNET"
    );

    set_indicator(
        G,
        "wm/concept/causal_factor/economic_and_commerce/economic_activity/market/price_or_cost/food_price",
        "Consumer price index",
        "WDI"
    );

    set_indicator(
        G,
        "wm/concept/indicator_and_reported_property/conflict/population_displacement",
        "Internally displaced persons, total displaced by conflict and violence",
        "WDI"
    );

    set_indicator(
        G,
        "wm/concept/causal_factor/condition/tension",
        "Conflict incidences",
        "None"
    );
}


int main() {
  string inflation = "wm/concept/causal_factor/economic_and_commerce/economic "
    "activity/market/inflation";
  string migration =
    "wm/concept/causal_factor/social_and_political/migration/human_migration";
  string food_security = "wm/concept/causal_factor/condition/food_security";

  vector<CausalFragment> causal_fragments = {
    {{"large", -1, inflation}, {"small", 1, migration}},
    {{"large", 1, migration}, {"small", -1, food_security}},
    {{"large", 1, migration}, {"small", -1, food_security}},
  };

  //AnalysisGraph G = AnalysisGraph::from_causal_fragments(causal_fragments);
  //r = RNG.rng();
  //r.set_seed(2018);
  AnalysisGraph G = create_base_CAG("../data/Model4.json");
  curate_indicators(G);
  G.data_heuristic = false;
  //G.parameterize("South Sudan", "Jonglei", "", 2017, 4, {});

  string rankdir = "TB";
  string node_to_highlight = "wm/concept/causal_factor/condition/food_insecurity";
  int label_depth = 1;
  bool simplified_labels = false;
    G.to_png(
        "Oct2019EvalCAG.png",
        simplified_labels,
        label_depth,
        node_to_highlight,
        rankdir
    );
  /*
    string country = "South Sudan";
    int res = 2;
    int burn = 10;
    bool use_heuristic = false;
    G.train_model(
        2014,
        6,
        2016,
        3,
        res,
        burn,
        country
    );

    G.generate_prediction(2016, 3, 2016, 7);
    */
}

