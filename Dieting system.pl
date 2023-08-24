% Facts about foods and their properties
food_properties(apple, [low_glycemic_index, low_sodium]).
food_properties(banana, [medium_glycemic_index, low_sodium]).
food_properties(carrot, [low_glycemic_index, low_sodium]).
food_properties(potato, [high_glycemic_index, low_sodium]).
food_properties(spinach, [low_glycemic_index, low_sodium]).
food_properties(salmon, [low_glycemic_index, low_sodium]).
food_properties(nuts, [low_glycemic_index, low_sodium]).
food_properties(sweets, [high_glycemic_index, low_sodium]).

% Rules for suggesting a diet based on disease
suggest_diet(Disease, Foods) :-
    findall(Food, (food_properties(Food, Properties), suitable_for_disease(Properties, Disease)), Foods).

suitable_for_disease(Properties, Disease) :-
    disease_properties(Disease, AllowedProperties),
    subset(AllowedProperties, Properties).

% Facts about disease properties
disease_properties(diabetes, [low_glycemic_index, low_sodium]).
disease_properties(hypertension, [low_sodium]).
