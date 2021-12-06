model_name='"nch 130nm_bulk"';
model_type='nmos';

[status,result] = system(strcat('python .\read_to_matlab_variable.py'," ",model_name," ",model_type));
nch = jsondecode(result);

model_name='"pch 130nm_bulk"';
model_type='pmos'
[status,result] = system(strcat('python .\read_to_matlab_variable.py'," ",model_name," ",model_type));
pch = jsondecode(result);