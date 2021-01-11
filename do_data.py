from random import randint, choice

file_name = 'data23mb.txt'
rows = 1000*1000 # ~ around 23mb

#file_name = 'data10gb.txt'
#rows = 1000*1000*400 # ~ around  10GB

cities = ['Yamoussoukro', 'Abu Dhabi','Abuja','Accra','Adamstown','Addis Ababa','Aden','Sana\'a','Algiers','Alofi',
          'Amman','Amsterdam','The Hague','Andorra la Vella','Ankara','Antananarivo',
          'Apia','Ashgabat','Asmara','Asunción','Athens','Avarua','Baghdad','Baku','Bamako','Bandar Seri Begawan',
          'Bangkok','Bangui','Banjul','Basseterre','Beijing','Beirut','Belgrade','Belmopan',
          'Berlin','Bern (de facto)','Bishkek','Bissau','Bloemfontein','Cape Town','Pretoria','Bogotá',
          'Brades Estate','Plymouth','Brasília','Bratislava','Brazzaville','Bridgetown','Brussels',
          'Bucharest','Budapest','Buenos Aires','Cairo','Canberra','Caracas','Castries','Cetinje','Podgorica',
          'Charlotte Amalie','Chișinău','Cockburn Town','Colombo','Sri Jayawardenepura Kotte','Conakry','Copenhagen',
          'Cotonou','Porto-Novo','Dakar','Damascus','Dar es Salaam','Dodoma','Dhaka','Dili','Djibouti','Doha',
          'Douglas','Dublin','Dushanbe','El Aaiún','Tifariti','Flying Fish Cove','Freetown','Funafuti','Gaborone',
          'George Town','Georgetown','Georgetown','Gibraltar','Gitega',
          'Bujumbura','Guatemala City','Gustavia','Hagåtña','Hamilton','Hanoi','Harare','Hargeisa',
          'Havana','Helsinki','Honiara','Islamabad','Jakarta','Jamestown','Jerusalem','Ramallah',
          'Juba','Kabul','Kampala','Kathmandu','Khartoum','Kigali','King Edward Point','Kingston',
          'Kingston','Kingstown','Kinshasa','Kuala Lumpur','Putrajaya','Kuwait City','Kyiv','La Paz',
          'Sucre','Libreville','Lilongwe','Lima','Lisbon','Ljubljana','Lobamba','Mbabane','Lomé','London',
          'Luanda','Lusaka','Luxembourg','Madrid','Majuro','Malabo','Malé','Managua','Manama','Manila',
          'Maputo','Mariehamn','Marigot','Maseru','Mata Utu','Mexico City','Minsk','Mogadishu','Monaco',
          'Monrovia','Montevideo','Moroni','Moscow','Muscat','Nairobi','Nassau','Naypyidaw','N\'Djamena',
          'New Delhi','Ngerulmud','Niamey','Nicosia','Nouakchott','Nouméa','Nukuʻalofa','Nur-Sultan',
          'Nuuk','Oranjestad','Oslo','Ottawa','Ouagadougou','Pago Pago','Palikir','Panama City','Papeete',
          'Paramaribo','Paris','Philipsburg','Phnom Penh','Port Louis','Port Moresby','Port Vila','Port-au-Prince',
          'Port of Spain','Prague','Praia','Pristina','Pyongyang','Quito','Rabat','Reykjavík','Riga','Riyadh',
          'Road Town','Rome','Roseau','Saipan','San José','San Juan','San Marino','San Salvador','Santiago',
          'Valparaíso','Santo Domingo','São Tomé','Sarajevo','Seoul','Singapore','Skopje','Sofia','South Tarawa',
          'St. George\'s','St. Helier','St. John\'s','St. Peter Port','St. Pierre','Stanley','Stepanakert',
          'Stockholm','Sukhumi','Suva','Taipei','Tallinn','Tashkent','Tbilisi','Tegucigalpa','Tehran',
          'Thimphu','Tirana','Tokyo','Tórshavn','Tripoli','Tskhinvali','Tunis','Ulaanbaatar','Vaduz',
          'Valletta','The Valley','Vatican City','Victoria','Vienna','Vientiane','Vilnius',
          'Warsaw','Washington. D.C.','Wellington','West Island','Willemstad','Windhoek','Yaoundé','Yaren','Yerevan','Zagreb']

with open(file_name, 'w', encoding="utf-8") as f:
    f.write(f'id, amount, city\n')
    c = 0
    for i in range(0,rows):
        f.write(f'{i}, {randint(1,3000)}, {choice(cities)}\n')
        c += 1
        if c % 100000 == 0:
            print(f"{c//1000}k", end=".")

print('generating the file is finished!')
