clc;
clear;
data = table2cell(readtable("fileExcel.xlsx", "VariableNamingRule","preserve"));
roles = data(:, 2);
names = data(:, 1);
contractors = names(roles == "Исполнитель");
managers = names(roles == "Руководитель");

strContractors = "";
for i = 1:length(contractors)
    strContractors = strContractors + contractors(i) + "; ";
end

strManagers = "";
for i = 1:length(managers)
    strManagers = strManagers + managers(i) + "; ";
end

cell = {"Руководители", strManagers;
    "Исполнители", strContractors};
table = cell2table(cell, "VariableNames", ["Роли", "ФИО"]);
writetable(table, "outFile1.xlsx");

