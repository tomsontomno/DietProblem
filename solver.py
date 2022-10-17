from ortools.linear_solver import pywraplp
import csv


def main():
    # Instantiate a Glop solver and naming it.
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return

    with open('Nutrients.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    data.pop(0)

    weight = 90  # in kg

    # Nutrient minimums and maximums
    nutrients = [
        ['Energy with dietary fibre, equated (kJ)', 0, 11000],
        ['Energy, without dietary fibre, equated (kJ)', 0, 11000],
        ['Moisture (water) (g)', 0, solver.infinity()],
        ['Protein (g)', 80, solver.infinity()],
        ['Nitrogen (g)', 0, solver.infinity()],
        ['Fat, total (g)', 0, 100],
        ['Ash (g)', 0, solver.infinity()],
        ['Total dietary fibre (g)', 25, 150],
        ['Alcohol (g)', 0, 0],
        ['Fructose (g)', 0, solver.infinity()],
        ['Glucose (g)', 0, solver.infinity()],
        ['Sucrose(g)', 0, solver.infinity()],
        ['Maltose (g)', 0, solver.infinity()],
        ['Lactose (g)', 0, solver.infinity()],
        ['Galactose (g)', 0, solver.infinity()],
        ['Maltotrios (g)', 0, solver.infinity()],
        ['Total sugars (g)', 0, solver.infinity()],
        ['Added sugars (g)', 0, solver.infinity()],
        ['Free sugars (g)', 0, solver.infinity()],
        ['Starch (g)', 125, solver.infinity()],
        ['Dextrin (g)', 0, solver.infinity()],
        ['Glycerol (g)', 0, weight*4],
        ['Glycogen (g)', 0, solver.infinity()],
        ['Inulin (g)', 0, solver.infinity()],
        ['Erythritol (g)', 0, solver.infinity()],
        ['Maltitol (g)', 0, solver.infinity()],
        ['Mannitol (g)', 0, solver.infinity()],
        ['Xylitol (g)', 0, solver.infinity()],
        ['Maltodextrin (g)', 0, solver.infinity()],
        ['Oligosaccharides  (g)', 0, solver.infinity()],
        ['Polydextrose (g)', 0, 15],
        ['Raffinose (g)', 0, solver.infinity()],
        ['Stachyose (g)', 0, solver.infinity()],
        ['Sorbitol (g)', 0, 35],
        ['Resistant starch (g)', 0, solver.infinity()],
        ['Available carbohydrate, without sugar alcohols (g)', 0, solver.infinity()],
        ['Available carbohydrate, with sugar alcohols (g)', 0, solver.infinity()],
        ['Acetic acid (g)', 0, solver.infinity()],
        ['Citric acid (g)', 0, 0.1*weight],
        ['Fumaric acid (g)', 0, 0.5],
        ['Lactic acid (g)', 0, solver.infinity()],
        ['Malic acid(g)', 0, solver.infinity()],
        ['Oxalic acid (g)', 0, 200],
        ['Propionic acid (g)', 0, solver.infinity()],
        ['Quinic acid (g)', 0, solver.infinity()],
        ['Shikimic acid (g)', 0, solver.infinity()],
        ['Succinic acid (g)', 0, solver.infinity()],
        ['Tartaric acid (g)', 0, solver.infinity()],
        ['Aluminium (Al) (ug)', 0, solver.infinity()],
        ['Antimony (Sb) (ug)', 0, 0.000529*weight],
        ['Arsenic (As) (ug)', 0, 0.000003],
        ['Cadmium (Cd) (ug)', 0, 0.000023],
        ['Calcium (Ca) (mg)', 900, solver.infinity()],
        ['Chromium (Cr) (ug)', 0.000033, solver.infinity()],
        ['Chloride (Cl) (mg)', 0, 3.6],
        ['Cobalt (Co) (ug)', 0, 0.0014],
        ['Copper (Cu) (mg)', 1, solver.infinity()],
        ['Fluoride (F) (ug)', 0, solver.infinity()],
        ['Iodine (I) (ug)', 150, solver.infinity()],
        ['Iron (Fe) (mg)', 9, solver.infinity()],
        ['Lead (Pb) (ug)', 0, solver.infinity()],
        ['Magnesium (Mg) (mg)', 400, solver.infinity()],
        ['Manganese (Mn) (mg)', 2.3, solver.infinity()],
        ['Mercury (Hg) (ug)', 0, 0.1*weight],
        ['Molybdenum (Mo) (ug)', 0, 60],
        ['Nickel (Ni) (ug)', 0, 150],
        ['Phosphorus (P) (mg)', 3500, solver.infinity()],
        ['Potassium (K) (mg)', 2000, solver.infinity()],
        ['Selenium (Se) (ug)', 55, solver.infinity()],
        ['Sodium (Na) (mg)', 0, 2300],
        ['Sulphur (S) (mg)', 0, 14*weight],
        ['Tin (Sn) (ug)', 0, 3],
        ['Zinc (Zn) (mg)', 12, solver.infinity()],
        ['Retinol (preformed vitamin A) (ug)', 900, 3000],
        ['Alpha-carotene (ug)', 0, solver.infinity()],
        ['Beta-carotene (ug)', 30, 3500],
        ['Cryptoxanthin (ug)', 0, solver.infinity()],
        ['Beta-carotene equivalents (provitamin A) (ug)', 0, solver.infinity()],
        ['Vitamin A retinol equivalents (ug)', 0, solver.infinity()],
        ['Lutein (ug)', 0, solver.infinity()],
        ['Lycopene (ug)', 0, solver.infinity()],
        ['Xanthophyl (ug)', 0, 30000],
        ['Thiamin (B1) (mg)', 1.3, solver.infinity()],
        ['Riboflavin (B2) (mg)', 1.4, solver.infinity()],
        ['Niacin (B3) (mg)', 17, solver.infinity()],
        ['Niacin derived from tryptophan (mg)', 0, solver.infinity()],
        ['Niacin derived equivalents (mg)', 0, solver.infinity()],
        ['Pantothenic acid (B5) (mg)', 5, solver.infinity()],
        ['Pyridoxine (B6) (mg)', 1.5, solver.infinity()],
        ['Biotin (B7) (ug)', 20, 200],
        ['Cobalamin (B12) (ug)', 2.4, solver.infinity()],
        ['Folate, natural (ug)', 0, solver.infinity()],
        ['Folic acid (ug)', 0, solver.infinity()],
        ['Total folates (ug)', 0, solver.infinity()],
        ['Dietary folate equivalents (ug)', 0, solver.infinity()],
        ['Vitamin C (mg)', 80, solver.infinity()],
        ['Cholecalciferol (D3) (ug)', 0, solver.infinity()],
        ['Ergocalciferol (D2) (ug)', 0, solver.infinity()],
        ['25-hydroxy cholecalciferol (25-OH D3) (ug)', 0, solver.infinity()],
        ['25-hydroxy ergocalciferol (25-OH D2) (ug)', 0, solver.infinity()],
        ['Vitamin D3 equivalents (ug)', 0, solver.infinity()],
        ['Alpha tocopherol (mg)', 0, solver.infinity()],
        ['Alpha tocotrienol (mg)', 0, solver.infinity()],
        ['Beta tocopherol (mg)', 0, solver.infinity()],
        ['Beta tocotrienol (mg)', 0, solver.infinity()],
        ['Delta tocopherol (mg)', 0, solver.infinity()],
        ['Delta tocotrienol (mg)', 0, solver.infinity()],
        ['Gamma tocopherol (mg)', 0, solver.infinity()],
        ['Gamma tocotrienol (mg)', 0, solver.infinity()],
        ['Vitamin E (mg)', 0, solver.infinity()],
        ['C4 (%T)', 0, solver.infinity()],
        ['C6 (%T)', 0, solver.infinity()],
        ['C8 (%T)', 0, solver.infinity()],
        ['C10 (%T)', 0, solver.infinity()],
        ['C11 (%T)', 0, solver.infinity()],
        ['C12 (%T)', 0, solver.infinity()],
        ['C13 (%T)', 0, solver.infinity()],
        ['C14 (%T)', 0, solver.infinity()],
        ['C15 (%T)', 0, solver.infinity()],
        ['C16 (%T)', 0, solver.infinity()],
        ['C17 (%T)', 0, solver.infinity()],
        ['C18 (%T)', 0, solver.infinity()],
        ['C19 (%T)', 0, solver.infinity()],
        ['C20 (%T)', 0, solver.infinity()],
        ['C21 (%T)', 0, solver.infinity()],
        ['C22 (%T)', 0, solver.infinity()],
        ['C23 (%T)', 0, solver.infinity()],
        ['C24 (%T)', 0, solver.infinity()],
        ['Total saturated fatty acids, equated (%T)', 0, solver.infinity()],
        ['C10:1 (%T)', 0, solver.infinity()],
        ['C12:1 (%T)', 0, solver.infinity()],
        ['C14:1 (%T)', 0, solver.infinity()],
        ['C15:1 (%T)', 0, solver.infinity()],
        ['C16:1 (%T)', 0, solver.infinity()],
        ['C17:1 (%T)', 0, solver.infinity()],
        ['C18:1 (%T)', 0, solver.infinity()],
        ['C18:1w5 (%T)', 0, solver.infinity()],
        ['C18:1w6 (%T)', 0, solver.infinity()],
        ['C18:1w7 (%T)', 0, solver.infinity()],
        ['C18:1w9 (%T)', 0, solver.infinity()],
        ['C20:1 (%T)', 0, solver.infinity()],
        ['C20:1w9 (%T)', 0, solver.infinity()],
        ['C20:1w13 (%T)', 0, solver.infinity()],
        ['C20:1w11 (%T)', 0, solver.infinity()],
        ['C22:1 (%T)', 0, solver.infinity()],
        ['C22:1w9 (%T)', 0, solver.infinity()],
        ['C22:1w11 (%T)', 0, solver.infinity()],
        ['C24:1 (%T)', 0, solver.infinity()],
        ['C24:1w9 (%T)', 0, solver.infinity()],
        ['C24:1w11 (%T)', 0, solver.infinity()],
        ['C24:1w13 (%T)', 0, solver.infinity()],
        ['Total monounsaturated fatty acids, equated (%T)', 0, solver.infinity()],
        ['C12:2 (%T)', 0, solver.infinity()],
        ['C16:2w4 (%T)', 0, solver.infinity()],
        ['C16:3 (%T)', 0, solver.infinity()],
        ['C18:2w6 (%T)', 0, solver.infinity()],
        ['C18:3w3 (%T)', 0, solver.infinity()],
        ['C18:3w4 (%T)', 0, solver.infinity()],
        ['C18:3w6 (%T)', 0, solver.infinity()],
        ['C18:4w1 (%T)', 0, solver.infinity()],
        ['C18:4w3 (%T)', 0, solver.infinity()],
        ['C20:2 (%T)', 0, solver.infinity()],
        ['C20:2w6 (%T)', 0, solver.infinity()],
        ['C20:3 (%T)', 0, solver.infinity()],
        ['C20:4 (%T)', 0, solver.infinity()],
        ['C20:3w3 (%T)', 0, solver.infinity()],
        ['C20:3w6 (%T)', 0, solver.infinity()],
        ['C20:4w3 (%T)', 0, solver.infinity()],
        ['C20:4w6 (%T)', 0, solver.infinity()],
        ['C20:5w3 (%T)', 0, solver.infinity()],
        ['C21:5w3 (%T)', 0, solver.infinity()],
        ['C22:2 (%T)', 0, solver.infinity()],
        ['C22:2w6 (%T)', 0, solver.infinity()],
        ['C22:4w6 (%T)', 0, solver.infinity()],
        ['C22:5w3 (%T)', 0, solver.infinity()],
        ['C22:5w6 (%T)', 0, solver.infinity()],
        ['C22:6w3 (%T)', 0, solver.infinity()],
        ['Total polyunsaturated fatty acids, equated (%T)', 0, solver.infinity()],
        ['Total long chain omega 3 fatty acids, equated (%T)', 0, solver.infinity()],
        ['Total undifferentiated fatty acids (%T)', 0, solver.infinity()],
        ['Total trans fatty acids, imputed (%T)', 0, solver.infinity()],
        ['C4 (g)', 0, solver.infinity()],
        ['C6 (g)', 0, solver.infinity()],
        ['C8 (g)', 0, solver.infinity()],
        ['C10 (g)', 0, solver.infinity()],
        ['C11 (g)', 0, solver.infinity()],
        ['C12 (g)', 0, solver.infinity()],
        ['C13 (g)', 0, solver.infinity()],
        ['C14 (g)', 0, solver.infinity()],
        ['C15 (g)', 0, solver.infinity()],
        ['C16 (g)', 0, solver.infinity()],
        ['C17 (g)', 0, solver.infinity()],
        ['C18 (g)', 0, solver.infinity()],
        ['C19 (g)', 0, solver.infinity()],
        ['C20 (g)', 0, solver.infinity()],
        ['C21 (g)', 0, solver.infinity()],
        ['C22 (g)', 0, solver.infinity()],
        ['C23 (g)', 0, solver.infinity()],
        ['C24 (g)', 0, solver.infinity()],
        ['Total saturated fatty acids, equated (g)', 0, solver.infinity()],
        ['C10:1 (g)', 0, solver.infinity()],
        ['C12:1 (g)', 0, solver.infinity()],
        ['C14:1 (g)', 0, solver.infinity()],
        ['C15:1 (g)', 0, solver.infinity()],
        ['C16:1 (g)', 0, solver.infinity()],
        ['C17:1 (g)', 0, solver.infinity()],
        ['C18:1 (g)', 0, solver.infinity()],
        ['C18:1w5 (mg)', 0, solver.infinity()],
        ['C18:1w6 (mg)', 0, solver.infinity()],
        ['C18:1w7 (g)', 0, solver.infinity()],
        ['C18:1w9 (mg)', 0, solver.infinity()],
        ['C20:1 (g)', 0, solver.infinity()],
        ['C20:1w9 (mg)', 0, solver.infinity()],
        ['C20:1w13 (mg)', 0, solver.infinity()],
        ['C20:1w11 (mg)', 0, solver.infinity()],
        ['C22:1 (g)', 0, solver.infinity()],
        ['C22:1w9 (mg)', 0, solver.infinity()],
        ['C22:1w11 (mg)', 0, solver.infinity()],
        ['C24:1 (g)', 0, solver.infinity()],
        ['C24:1w9 (mg)', 0, solver.infinity()],
        ['C24:1w11 (mg)', 0, solver.infinity()],
        ['C24:1w13 (mg)', 0, solver.infinity()],
        ['Total monounsaturated fatty acids, equated (g)', 0, solver.infinity()],
        ['C12:2 (g)', 0, solver.infinity()],
        ['C16:2w4 (mg)', 0, solver.infinity()],
        ['C16:3 (g)', 0, solver.infinity()],
        ['C18:2w6 (g)', 0, solver.infinity()],
        ['C18:3w3 (g)', 0, solver.infinity()],
        ['C18:3w4 (g)', 0, solver.infinity()],
        ['C18:3w6 (mg)', 0, solver.infinity()],
        ['C18:4w1 (g)', 0, solver.infinity()],
        ['C18:4w3 (mg)', 0, solver.infinity()],
        ['C20:2 (mg)', 0, solver.infinity()],
        ['C20:2w6 (mg)', 0, solver.infinity()],
        ['C20:3 (mg)', 0, solver.infinity()],
        ['C20:3w3 (mg)', 0, solver.infinity()],
        ['C20:3w6 (mg)', 0, solver.infinity()],
        ['C20:4 (g)', 0, solver.infinity()],
        ['C20:4w3 (mg)', 0, solver.infinity()],
        ['C20:4w6 (mg)', 0, solver.infinity()],
        ['C20:5w3 (mg)', 0, solver.infinity()],
        ['C21:5w3 (g)', 0, solver.infinity()],
        ['C22:5w3 (mg)', 0, solver.infinity()],
        ['C22:4w6 (mg)', 0, solver.infinity()],
        ['C22:2 (g)', 0, solver.infinity()],
        ['C22:2w6 (mg)', 0, solver.infinity()],
        ['C22:5w6 (g)', 0, solver.infinity()],
        ['C22:6w3 (mg)', 0, solver.infinity()],
        ['Total polyunsaturated fatty acids, equated (g)', 0, solver.infinity()],
        ['Total long chain omega 3 fatty acids, equated (mg)', 300, solver.infinity()],
        ['Total undifferentiated fatty acids, mass basis basis (mg)', 0, solver.infinity()],
        ['Total trans fatty acids, imputed (mg)', 0, solver.infinity()],
        ['Caffeine (mg)', 0, 400],
        ['Cholesterol (mg)', 0, 200],
        ['Alanine (mg/gN)', 1800, 6500],
        ['Arginine (mg/gN)', 1500, 7000],
        ['Aspartic acid (mg/gN)', 0, solver.infinity()],
        ['Cystine plus cysteine (mg/gN)', 0, solver.infinity()],
        ['Glutamic acid (mg/gN)', 0, solver.infinity()],
        ['Glycine (mg/gN)', 0, solver.infinity()],
        ['Histidine (mg/gN)', 0, solver.infinity()],
        ['Isoleucine (mg/gN)', 0, solver.infinity()],
        ['Leucine (mg/gN)', 0, solver.infinity()],
        ['Lysine (mg/gN)', 0, solver.infinity()],
        ['Methionine (mg/gN)', 0, solver.infinity()],
        ['Phenylalanine (mg/gN)', 0, solver.infinity()],
        ['Proline (mg/gN)', 0, solver.infinity()],
        ['Serine (mg/gN)', 0, solver.infinity()],
        ['Threonine (mg/gN)', 0, solver.infinity()],
        ['Tyrosine (mg/gN)', 0, solver.infinity()],
        ['Tryptophan (mg/gN)', 0, solver.infinity()],
        ['Valine (mg/gN)', 0, solver.infinity()],
        ['Alanine (mg)', 0, solver.infinity()],
        ['Arginine (mg)', 0, solver.infinity()],
        ['Aspartic acid (mg)', 0, solver.infinity()],
        ['Cystine plus cysteine (mg)', 0, solver.infinity()],
        ['Glutamic acid (mg)', 0, solver.infinity()],
        ['Glycine (mg)', 2000, solver.infinity()],
        ['Histidine (mg)', 14*weight, solver.infinity()],
        ['Isoleucine (mg)', 19*weight, solver.infinity()],
        ['Leucine (mg)', 4400, solver.infinity()],
        ['Lysine (mg)', 1000, solver.infinity()],
        ['Methionine (mg)', 1300, solver.infinity()],
        ['Phenylalanine (mg)', 9.1*weight, solver.infinity()],
        ['Proline (mg)', 0, solver.infinity()],
        ['Serine (mg)', 2000, solver.infinity()],
        ['Threonine (mg)', 500, solver.infinity()],
        ['Tyrosine (mg)', 150, solver.infinity()],
        ['Tryptophan (mg)', 250, solver.infinity()],
        ['Valine (mg)', 30*weight, solver.infinity()],
    ]

    # Declare an array to hold our variables.
    max_of_a_kind = 200  # grams
    foods = []
    max_cheese = 100  # grams
    for item in data:
        if "Cheese" in item[0]:
            foods.append(solver.NumVar(0.0, max_cheese / 100, item[0]))
        else:
            foods.append(solver.NumVar(0.0, max_of_a_kind / 100, item[0]))

    print('Number of variables =', solver.NumVariables())

    # Create the constraints, one per nutrient.
    constraints = []
    for i, nutrient in enumerate(nutrients):
        constraints.append(solver.Constraint(nutrient[1], nutrient[2]))
        for j, item in enumerate(data):
            constraints[i].SetCoefficient(foods[j], float(str(item[i + 1]).replace(",", "")))

    print('Number of constraints =', solver.NumConstraints())

    # Objective function: Minimize the sum of (price-normalized) foods.
    objective = solver.Objective()
    optimize = 1
    for food in foods:
        objective.SetCoefficient(food, optimize)
    objective.SetMinimization()

    status = solver.Solve()

    # Check that the problem has an optimal solution.
    if status != solver.OPTIMAL:
        print('The problem does not have an optimal solution!')
        if status == solver.FEASIBLE:
            print('A potentially suboptimal solution was found.')
        else:
            print('The solver could not solve the problem.')
            exit(1)

    # Display the amounts (in dollars) to purchase of each food.
    nutrients_result = [0] * len(nutrients)
    print('\nDaily Foods:')
    ignored = 0
    for i, food in enumerate(foods):
        ignore_bound = 5  # grams
        if food.solution_value()*100 > ignore_bound:
            print('{}: {:.4f} grams'.format(data[i][0], food.solution_value()*100))
            for j, _ in enumerate(nutrients):
                nutrients_result[j] += float(str(data[i][j + 1]).replace(",", "")) * food.solution_value()
        elif food.solution_value() > 0:
            # under ignore_bound
            ignored += 1
    print("ignored:", ignored)

    print('\nNutrients per day:')
    for i, nutrient in enumerate(nutrients):
        if nutrients_result[i] != 0 and (nutrient[1] != 0 or nutrient[2] != solver.infinity()):
            print('{:.3f} (min {}, max {}) --- {}:  '.format(nutrients_result[i], nutrient[1], nutrient[2], nutrient[0]))

    print('\nAdvanced usage:')
    print('Problem solved in ', solver.wall_time(), ' milliseconds')
    print('Problem solved in ', solver.iterations(), ' iterations')


if __name__ == '__main__':
    main()