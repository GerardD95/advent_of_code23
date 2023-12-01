  # # convert written numbers to digits
  # prev = ''
  # for i, char in enumerate(text):

  #   #  check if char is in number_mapping
  #   for k,v in number_mapping.items():

  #     # get char of key by index
  #     if len(prev) != 0: 
  #       try:
  #         if char == k[len(prev)]:
  #           prev += char
  #           if prev in number_mapping:
  #             text = text.replace(prev, number_mapping[prev])
  #             prev = ''
  #           break
          
  #         # new_text = convert_written_numbers(text[i:])
  #         # text = text[:i] + new_text

  #       except IndexError:
  #         continue

  #     elif char == k[0]:
  #       prev += char
  #       break
      
  return text
