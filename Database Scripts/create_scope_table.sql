CREATE TABLE scope(
   Id INT GENERATED ALWAYS AS IDENTITY,
   week int not null,
   low int not null,
   average int not null,
   high int not null,
   points int not null,	
   PRIMARY KEY(Id)
); 