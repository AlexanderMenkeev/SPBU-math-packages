clc;
clear;
data = readtable("Data_18032020.xlsx", "VariableNamingRule","preserve");

%3.1 Определить и записать в отдельный стобец возраст участников
birthdays = table2array(data(:, "дата рождения"));
now = datetime('now');
age = between(birthdays, now, {'years', 'months'});
data(:, "Возраст") = array2table(age);

%3.2 Определить публикации, которые имеют id1 и id2 длиной 11 символов
id1 = table2array(data(:, "id1"));
id2 = table2array(data(:, "id2"));

id1 = strlength(id1) == 11;
id2 = strlength(id2) == 11;

data(:, "id1 длиной 11 символов") = array2table(id1);
data(:, "id2 длиной 11 символов") = array2table(id2);

%3.3 Посчитать коэффициент отношения числа внутренних авторов ко всем
totalNum = table2array(data(:, "Кол-во всего авторов"));
innerNum = table2array(data(:, "Кол-во авторов внутренних"));
k = innerNum ./ totalNum;

data(:, "Коэффициент отношения") = array2table(k);

%3.4 В зависимости от коэффициента в пункте 3.3 присвоить значение в
%дополнительный столбец
for i = 1:length(k)
    if k(i) <= 0.1
        k(i) = 0.1;
    elseif k(i) <= 0.2
        k(i) = 0.2;
    elseif k(i) <= 0.3
        k(i) = 0.4;
    elseif k(i) <= 0.4
        k(i) = 0.6;
    elseif k(i) <= 0.5
        k(i) = 0.8;
    else
        k(i) = 1;
    end
end

data(:, "Значение") = array2table(k);

writetable(data, "outFile2.xlsx");
