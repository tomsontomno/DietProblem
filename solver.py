from ortools.linear_solver import pywraplp
import csv


# sublist: enter list[list]
# element: enter index of element, that should be sorted after
# 0 for ASC, 1 for DESC order
def Sort(sublist: list, element: int, asc_desc: int = 1):
    sublist.sort(key=lambda x: x[element])
    if asc_desc == 1:
        sublist.reverse()
    return sublist


def main(param_blacklist: list[int] = None):
    if param_blacklist is None:
        param_blacklist = []
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return -1

    # init the personal variables
    weight = 90  # in kg (used for some boundaries)
    ignore_bound = 5  # don't print any food under "ignore_bound" grams
    for_x_days = 1  # output the foods for x days (1 = daily diet, eat the same foods every day)
    max_of_a_kind = 200  # no food will be eaten more than (max_of_a_kind) grams in ONE day.

    with open('Nutrients_ID.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    data.pop(0)

    # every nutrient's lower and upper boundaries in the given unit
    nutrients = [
        ['Energy with dietary fibre, equated (kJ)', 0, 8480],
        ['Energy, without dietary fibre, equated (kJ)', 0, solver.infinity()],
        ['Moisture (water) (g)', 0, solver.infinity()],
        ['Protein (g)', 1.1*weight, solver.infinity()],
        ['Nitrogen (g)', 0, solver.infinity()],
        ['Fat, total (g)', 0, 95],
        ['Ash (g)', 0, solver.infinity()],
        ['Total dietary fibre (g)', 20, 150],
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
        ['Starch (g)', 100, solver.infinity()],
        ['Dextrin (g)', 0, solver.infinity()],
        ['Glycerol (g)', 0, weight * 4],
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
        ['Citric acid (g)', 0, 0.1 * weight],
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
        ['Antimony (Sb) (ug)', 0, 0.000529 * weight],
        ['Arsenic (As) (ug)', 0, 0.000003],
        ['Cadmium (Cd) (ug)', 0, 0.000023],
        ['Calcium (Ca) (mg)', 700, solver.infinity()],
        ['Chromium (Cr) (ug)', 0.000033, solver.infinity()],
        ['Chloride (Cl) (mg)', 0, 3.6],
        ['Cobalt (Co) (ug)', 0, 0.0014],
        ['Copper (Cu) (mg)', 1, solver.infinity()],
        ['Fluoride (F) (ug)', 0, solver.infinity()],
        ['Iodine (I) (ug)', 0, solver.infinity()],
        ['Iron (Fe) (mg)', 9, solver.infinity()],
        ['Lead (Pb) (ug)', 0, solver.infinity()],
        ['Magnesium (Mg) (mg)', 400, solver.infinity()],
        ['Manganese (Mn) (mg)', 2.0, solver.infinity()],
        ['Mercury (Hg) (ug)', 0, 0.1 * weight],
        ['Molybdenum (Mo) (ug)', 0, 2000],
        ['Nickel (Ni) (ug)', 0, 50],
        ['Phosphorus (P) (mg)', 800, 1900],
        ['Potassium (K) (mg)', 4700, solver.infinity()],
        ['Selenium (Se) (ug)', 55, solver.infinity()],
        ['Sodium (Na) (mg)', 0, 2300],
        ['Sulphur (S) (mg)', 0, 15 * weight],
        ['Tin (Sn) (ug)', 0, 0],
        ['Zinc (Zn) (mg)', 11, solver.infinity()],
        ['Retinol (preformed vitamin A) (ug)', 700, solver.infinity()],
        ['Alpha-carotene (ug)', 3000, solver.infinity()],
        ['Beta-carotene (ug)', 4000, solver.infinity()],
        ['Cryptoxanthin (ug)', 0, solver.infinity()],
        ['Beta-carotene equivalents (provitamin A) (ug)', 0, solver.infinity()],
        ['Vitamin A retinol equivalents (ug)', 0, solver.infinity()],
        ['Lutein (ug)', 0, solver.infinity()],
        ['Lycopene (ug)', 0, solver.infinity()],
        ['Xanthophyl (ug)', 0, solver.infinity()],
        ['Thiamin (B1) (mg)', 1.2, solver.infinity()],
        ['Riboflavin (B2) (mg)', 1.3, solver.infinity()],
        ['Niacin (B3) (mg)', 16, solver.infinity()],
        ['Niacin derived from tryptophan (mg)', 0, solver.infinity()],
        ['Niacin derived equivalents (mg)', 0, solver.infinity()],
        ['Pantothenic acid (B5) (mg)', 5, solver.infinity()],
        ['Pyridoxine (B6) (mg)', 1.3, solver.infinity()],
        ['Biotin (B7) (ug)', 30, 200],
        ['Cobalamin (B12) (ug)', 2, solver.infinity()],
        ['Folate, natural (ug)', 0, solver.infinity()],
        ['Folic acid (ug)', 0, solver.infinity()],
        ['Total folates (ug)', 0, solver.infinity()],
        ['Dietary folate equivalents (ug)', 0, solver.infinity()],
        ['Vitamin C (mg)', 90, solver.infinity()],
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
        ['Total long chain omega 3 fatty acids, equated (mg)', 250, solver.infinity()],
        ['Total undifferentiated fatty acids, mass basis basis (mg)', 0, solver.infinity()],
        ['Total trans fatty acids, imputed (mg)', 0, solver.infinity()],
        ['Caffeine (mg)', 0, 400],
        ['Cholesterol (mg)', 0, 300],
        ['Alanine (mg/gN)', 2000, 6500],
        ['Arginine (mg/gN)', 6000, 30000],
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
        ['Glutamic acid (mg)', 2000, solver.infinity()],
        ['Glycine (mg)', 0, solver.infinity()],
        ['Histidine (mg)', 0, solver.infinity()],
        ['Isoleucine (mg)', 0, solver.infinity()],
        ['Leucine (mg)', 0, solver.infinity()],
        ['Lysine (mg)', 0, solver.infinity()],
        ['Methionine (mg)', 0, solver.infinity()],
        ['Phenylalanine (mg)', 0, solver.infinity()],
        ['Proline (mg)', 0, solver.infinity()],
        ['Serine (mg)', 0, solver.infinity()],
        ['Threonine (mg)', 0, solver.infinity()],
        ['Tyrosine (mg)', 0, solver.infinity()],
        ['Tryptophan (mg)', 0, solver.infinity()],
        ['Valine (mg)', 0, solver.infinity()],
    ]

    # create array with the variables, that set the min,max boundaries for each food in Nutrients.csv
    ignore_bound = ignore_bound * for_x_days
    max_of_a_kind = max_of_a_kind * for_x_days  # grams
    foods = []

    # foods that have their ID on the blacklist will not be included in the "Daily Foods" and their max is set to 0
    blacklist = [356, 276, 355, 370, 371, 357, 364, 1262, 882, 55, 826, 795, 1077, 794, 1079, 1200, 792, 75, 1169, 740,
                 595, 480, 1207, 1209, 1211, 1215, 1203, 1217, 723, 1153]
    blacklist = blacklist + param_blacklist
    # foods in the reduced category will at most be eaten 1/2 the "max_of_a_kind" amount per day
    reduced = []
    # foods in the reduced category will at most be eaten 1/8 the "max_of_a_kind" amount per day
    extremely_reduced = [295, 294, 571]

    # custom reduction categories, that can be configured independently
    custom_reduction_var1 = 5
    custom_reduction1 = [363, 991, 997, 1000]
    custom_reduction_var2 = 4
    custom_reduction2 = []
    custom_reduction_var3 = 1
    custom_reduction3 = []

    # sets the min/max boundaries for every different food, in respect of categorical properties like "blacklist" and
    # "reduced" etc. and the "max_of_a_kind" parameter
    for item in data:
        if int(item[0]) in blacklist:
            foods.append(solver.NumVar(0.0, 0 / 100, item[1]))
        elif int(item[0]) in reduced:
            foods.append(solver.NumVar(0.0, (max_of_a_kind/2) / 100, item[1]))
        elif int(item[0]) in extremely_reduced:
            foods.append(solver.NumVar(0.0, (max_of_a_kind/8) / 100, item[1]))
        elif int(item[0]) in custom_reduction1:
            foods.append(solver.NumVar(0.0, (max_of_a_kind/custom_reduction_var1) / 100, item[1]))
        elif int(item[0]) in custom_reduction2:
            foods.append(solver.NumVar(0.0, (max_of_a_kind/custom_reduction_var2) / 100, item[1]))
        elif int(item[0]) in custom_reduction3:
            foods.append(solver.NumVar(0.0, (max_of_a_kind/custom_reduction_var3) / 100, item[1]))
        else:
            foods.append(solver.NumVar(0.0, max_of_a_kind / 100, item[1]))

    print('Number of variables =', solver.NumVariables())

    # creates the constraints
    constraints = []
    for i, nutrient in enumerate(nutrients):
        constraints.append(solver.Constraint(nutrient[1] * for_x_days, nutrient[2] * for_x_days))
        for j, item in enumerate(data):
            constraints[i].SetCoefficient(foods[j], float(str(item[i + 2]).replace(",", "")))

    print('Number of constraints =', solver.NumConstraints())

    # objective-function
    objective = solver.Objective()
    optimize = 1
    print("Optimize for", nutrients[optimize][0])

    for food in foods:
        objective.SetCoefficient(food, optimize)
    objective.SetMinimization()

    status = solver.Solve()

    # checks if the problem has an optimal solution.
    if status != solver.OPTIMAL:
        print('The problem does not have an optimal solution!')
        if status == solver.FEASIBLE:
            print('A potentially suboptimal solution was found.')
        else:
            print('The solver could not solve the problem.')
            return 1

    # prints the calculated optimal intake, presented as "daily foods"
    nutrients_result = [0] * len(nutrients)

    ignored = 0
    daily = []
    for i, food in enumerate(foods):
        # only consider the food in "Daily Foods", if and only if the solution_value() is higher than the "ignore_bound"
        if food.solution_value()*100 > ignore_bound:
            # daily[x] = [ID, name, value in grams, index in data]
            daily.append([data[i][0], data[i][1], food.solution_value()*100, i])
        elif food.solution_value() > 0:
            # 0 < food.solution_value() < ignore_bound, so the "ignored"-counter, increments
            ignored += 1

    # the "daily" list[list2], is sorted by a value in list 2 e.g. "ID" or "grams"
    daily = Sort(daily, 2)

    print('\nDaily Foods:')
    # Output of "Daily Foods"
    food_IDs = []
    amount_grams = 0
    for j, food in enumerate(daily):
        food_IDs.append(int(food[0]))
        print('{:.2f} grams, ID:{} - {}'.format(food[2], food[0], food[1]))
        amount_grams += int(food[2])

        # every nutrient of each food in "daily"-list is saved
        for k, _ in enumerate(nutrients):
            nutrients_result[k] += float(str(data[food[3]][k + 2]).replace(",", "")) * food[2]/100

    print("ignored:", ignored)
    print("Total weight:", amount_grams, "grams")

    # prints the daily nutrients, as well as the min and max boundaries for each of them
    # (ignores unbounded nutrients, which are not included in the diet)
    print('\nNutrients per day:')
    for i, nutrient in enumerate(nutrients):
        if not (nutrient[1] == 0 and nutrient[2] == solver.infinity()) and nutrients_result[i] > 0.001:
            if 0.975 < (nutrient[1] * for_x_days) / nutrients_result[i] < 1.025:
                print('--> {:.3f} (min {:.2f}, max {:.2f}) --- {}:  '.format(nutrients_result[i],
                                                                             (nutrient[1] * for_x_days),
                                                                             nutrient[2] * for_x_days, nutrient[0]))
            else:
                print(
                    '{:.3f} (min {:.2f}, max {:.2f}) --- {}:  '.format(nutrients_result[i], (nutrient[1] * for_x_days),
                                                                       nutrient[2] * for_x_days, nutrient[0]))

    print('Problem solved in ', solver.wall_time(), ' milliseconds')
    print('Problem solved in ', solver.iterations(), ' iterations')
    return food_IDs


if __name__ == '__main__':
    main()
