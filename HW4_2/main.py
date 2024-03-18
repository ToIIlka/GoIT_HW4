def get_cats_info(path):
    cats_info = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                cat = line.strip().split(',')
                cat_info = {
                    'id': cat[0],
                    'name': cat[1],
                    'age': int(cat[2])
                }
                cats_info.append(cat_info)
            
    except FileNotFoundError:
        print("Файл не знайдено.")
    except Exception as e:
        print(f"Виникла помилка: {e}")
    return cats_info
cats = get_cats_info('cats.txt')
for info in cats:
    print(info)