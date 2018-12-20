def create_dataset(file):
    dataset = dict()
    with open(file) as f:
        file_line = f.readline()
        if not file_line:
            return dataset
        file_line = f.readline()
        while file_line:
            [minimum_age, maximum_age, gender, population, zipcode, geo_id] = [element.strip() for element in
                                                                               file_line.rstrip().split(",")]
            if geo_id not in dataset:
                dataset[geo_id] = dict()
            if zipcode not in dataset[geo_id]:
                dataset[geo_id][zipcode] = dict()
            if population not in dataset[geo_id][zipcode]:
                dataset[geo_id][zipcode][population] = dict()
            dataset[geo_id][zipcode][population].update({
                gender: [maximum_age, minimum_age]
            })
            file_line = f.readline()
    return dataset


def create_dataset_4lines(file):
    dataset = dict()
    with open(file) as f:
        file_line = f.readline()
        if not file_line:
            return dataset
        file_line = f.readline()
        while file_line:
            [minimum_age, maximum_age, gender, population, zipcode, geo_id] = [element.strip() for element in
                                                                                    file_line.rstrip().split(",")]
            if minimum_age not in dataset:
                dataset[minimum_age] = dict()
            if maximum_age not in dataset[minimum_age]:
                dataset[minimum_age][maximum_age] = dict()
            dataset[minimum_age][maximum_age].update({
                gender: {population}
            })
            file_line = f.readline()
    return dataset
