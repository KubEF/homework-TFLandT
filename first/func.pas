function DiagNumberAndStart(k: integer): (integer, integer);
var
  n: integer;
  count: integer;
begin
  n := 1;
  count := 1;
  while count < k do
  begin
    n := n + 1;
    count := count + n;
  end;
  Result := (n, count - n + 1);
end;

function J(k: integer): integer;
var
  diagNum: integer;
  diagStart: integer;
begin
  (diagNum, diagStart) := DiagNumberAndStart(k);
  Result := k - diagStart + 1;
end;

function I(k: integer): integer;
var
  diagNum: integer;
  diagStart: integer;
begin
  (diagNum, diagStart) := DiagNumberAndStart(k);
  Result := diagNum + 1 - (k - diagStart + 1);
end.