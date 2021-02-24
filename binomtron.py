import random

students_list = [
    'Antoine','Arthur','Camille', 'Farid', 
    'Giovanny', 'Hatice', 'Joséphine', 'Julien', 
    'Kevin F.', 'Marie', 'Mickael', 'Phichet', 
    'Rachid', 'Tanguy', 'Valentin', 'Vivien', 'Kevin B.'
]

list_to_process = students_list[:]

def ask_size_group():
    """
        Ask for size of groups
        :return: the size of the groups
    """
    print ("Saisir le nombre approximatif de personnes voulu par groupe : 2, 3 ou 4")
    user_input = int(input())
    if user_input < 2 or user_input >4 :
        print("Merci d'entrer un chiffre compris entre 2 et 4 : ")
        return ask_size_group()
    return user_input

def generate_group(pool, size):
    """
        Generate groupe with given params.

        Parameters:
        
        pool(list) : base list
        size(int) : asked group size
        
        Returns: 
        list: list of groups
    """
    # initialise la liste de groupes
    groups = []
    # initialise le nombre de groupes par une "floor division"
    number_of_groups = len(pool) // size
    
  # Génère les groupes avec le nombre de groupes et la taille demandée de chaque groupe
    for group in range(number_of_groups):
        group = random.sample(pool, size)
        groups.append(group)
        
        # Retire les personnes déjà sélectionnées
        for el in group:
            pool.remove(el)

    # Si après distribution il reste des personnes, on les répartit dans les groupes existants.
    
    if len(pool) > 0:
        i = 0
        while i < len(pool) :
            groups[i].append(pool[i])
            i += 1
    return groups

def display_groups():
    """
        Display groups
    """
    groups = generate_group(list_to_process,ask_size_group())
    for i , x in enumerate(groups) :
        separator = ', '
        print("le groupe {} est composé de : {}".format(i+1, separator.join(x)))

display_groups()
