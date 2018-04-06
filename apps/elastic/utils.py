import copy

from apps.attribute.models import Attribute

query_body = {
    'query': {
        'bool': {
            'should': []
        }
    },
    # highlight : {
    #     encoder: 'html',
    #     fields : {
    #         comment : {}
    #     }
    # }
}

query_string_default = {
    'default': {
        'query_string': {
            'default_field': "*{0}*",
            'query': "{0}",
        }
    },
    'phone': {
        'query_string': {
            'default_field': "*{0}*",
            'query': "{0}~2",
            'analyzer': "whitespace",
            'lenient': True,
        }
    },
    'address': {
        'query_string': {
            'default_field': "*{}*",
            'query': "{}",
            'analyze_wildcard': True,
            'lenient': True,
            'fuzziness': 3,
        }
    }
}


def prepare_q2( jsonQuery):
    first_level_mapping = {}
    queryset = Attribute.objects.filter(mapping_type=1).exclude(
        entity_attribute__isnull=True).values('name', 'entity_attribute__name')

    for row_queryset in queryset:
        attribute_name = row_queryset['name']
        entity_attribute_name = row_queryset['entity_attribute__name']
        if entity_attribute_name in first_level_mapping.keys():
            first_level_mapping[entity_attribute_name].append(attribute_name)
        else:
            first_level_mapping[entity_attribute_name] = [attribute_name]


    fields = []
    queryItems = []

    query_string = query_string_default

    for key, value in jsonQuery.items():

        attr_names = first_level_mapping[key];

        for currentValue in attr_names:
            fields.append("*" + currentValue + "*")
            queryString = None
            if currentValue.find("phone")>-1:
                queryString = copy.deepcopy(query_string['phone'])
            elif currentValue.find("address")>-1:
                queryString = copy.deepcopy(query_string['address'])
            else:
                queryString = copy.deepcopy(query_string['default'])

            queryString['query_string']['default_field'] = queryString['query_string']['default_field'].format(currentValue)
            queryString['query_string']['query'] = queryString['query_string']['query'].format(value)
            queryItems.append(queryString)


    # Object.keys(jsonQuery).forEach((key) => {
    #     let value = jsonQuery[key];
    #
    #     let attr_mapping = _.findLast( first_level_mapping, {name:key});
    #     let attr_names = [];
    #     if (attr_mapping!=undefined)
    #         attr_names = attr_mapping.attr_names;
    #     else
    #         attr_names.push(key);
    #
    #     attr_names.forEach((currentValue, index) => {
    #
    #         fields.push("*"+currentValue+"*");
    #
    #         var queryString = null;
    #         if (currentValue.indexOf("phone")>-1) {
    #             queryString=JSON.parse(JSON.stringify(query_string.phone));
    #         } else if (currentValue.indexOf("address")>-1) {
    #             queryString=JSON.parse(JSON.stringify(query_string.address));
    #             //TODO using regexp to add '+' for every word in string
    #             value = value.replace(/(\w+)/g,"+$1");
    #         } else {
    #             queryString=JSON.parse(JSON.stringify(query_string.default));
    #         }
    #         queryString.query_string.default_field = format(queryString.query_string.default_field, currentValue);
    #         queryString.query_string.query = format( queryString.query_string.query, value);
    #         //let values = {};
    #         //let item = {};
    #         //item.default_field = "*"+key+"*";
    #         //item.query = jsonQuery[key];
    #         queryItems.push(queryString);
    #
    #     });
    # });
    #
    queryBody = copy.deepcopy(query_body)
    queryBody['query']['bool']['should'] = queryItems
    return queryBody
