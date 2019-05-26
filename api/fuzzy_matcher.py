import pandas as pd
from fuzzywuzzy import fuzz

def compare_company_names(profile_name, entity_name):

    ratio = fuzz.ratio(profile_name.lower(), entity_name.lower())

    return ratio

# Function to return company profiles desc by company_id.
def get_company_desc(company_id):

    profile_data = pd.read_csv("company_profiles.tsv",
                  sep='\t',
                  names=["id", "company_name", "website_url", "foundation_year", "city", "country"],
                  usecols=[0,1])

    desc = profile_data.loc[profile_data['id'] == company_id]['company_name'].to_string(index=False,header=False)

    return desc

# Return similar entities based on the company desc.
def get_similar_entities(company_id):

    company_desc = get_company_desc(company_id)
    entity_df = pd.read_csv("company_entities.tsv",
                            sep='\t',
                            names=["id", "company_name", "website_url", "foundation_year", "city", "country"])

    d_list = []
    entity_dict = {'id': None, 'company_name': None, 'website_url': None, 'foundation_year': None, 'city': None,
                   'country': None}
    # Iterate over dataframe.
    for index, row in entity_df.iterrows():
        entity_name = row['company_name']
        similarity = compare_company_names(company_desc, entity_name)

        if similarity > 75:
            print('Sucesso: ' + str(entity_name) + '- Similarity: ' + str(similarity))
            entity_dict["id"] = row["id"]
            entity_dict["company_name"] = row["company_name"]
            entity_dict["website_url"] = row["website_url"]
            entity_dict["foundation_year"] = row["foundation_year"]
            entity_dict["city"] = row["city"]
            entity_dict["country"] = row["country"]

            d_list.append(entity_dict.copy())

    #result = json.dumps(d_list, ensure_ascii=False)
    return d_list

if __name__ == '__main__':
    get_similar_entities(company_id=403)
