CREATE TABLE future_capabilities(
   Id INT GENERATED ALWAYS AS IDENTITY,
   points int not null,
   size VARCHAR (10) not null,
   capabilities_count int not null,
   PRIMARY KEY(Id)
); 