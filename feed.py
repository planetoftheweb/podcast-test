import yaml
import xml.etree.ElementTree as xml_tree

with open('feed.yaml', 'r') as file:
  yaml_data = yaml.safe_load(file)

  rss_element = xml_tree.Element('rss', {'version':'2.0',
    'xmlns:itunes':'http://www.itunes.com/dtds/podcast-1.0.dtd',
    'xmlns:content':'http://purl.org/rss/1.0/modules/content/'})

channel_element = xml_tree.SubElement(rss_element, 'channel')

xml_tree.SubElement(channel_element, 'title').text = yaml_data['title']

output_tree = xml_tree.ElementTree(rss_element)
output_tree.write('podcast.xml', encoding='UTF-8', xml_declaration=True)