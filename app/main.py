def get_human_age(cat_age: int, dog_age: int) -> list:
    human_cat = ((cat_age >= 15) + (cat_age >= 24)
                 + max(0, (cat_age - 24) // 4 * (cat_age >= 24)))

    human_dog = ((dog_age >= 15) + (dog_age >= 24)
                 + max(0, (dog_age - 24) // 5 * (dog_age >= 24)))

    return [human_cat, human_dog]
