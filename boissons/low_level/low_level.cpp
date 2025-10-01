
#include <iostream>
using namespace std;
#include <cpr/cpr.h>
#include <nlohmann/json.hpp>

using json = nlohmann::json;

class metier {
private:
  const char *nom;
  int remuneration;

public:
  metier(const char *n, float rem) {
    nom = n;
    remuneration = rem;
  }

  void afficher() {
    cout << "nom:" << nom << " , remuneration:" << remuneration << endl;
  }
};

class Localisation {
private:
  const char *nom;
  float taxes;
  float prix_m2;

public:
  Localisation(const char *n, float tax, float pr) {
    nom = n;
    taxes = tax;
    prix_m2 = pr;
  }

  void afficher() {
    cout << "nom:" << nom << " , taxes:" << taxes << " , prix_m2:" << prix_m2
         << "." << endl;
  }
};

int main() {

  cpr::Response r = cpr::Get(cpr::Url{"http://127.0.0.1:8000/localisation/1/"});
  cout << r.text;
  // nlohmann:: json data

  Localisation objet("Paris", 20, 100);
  objet.afficher();

  return 0;
}
