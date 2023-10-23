select u.Category, COUNT(*) AS VisitCount
from UniqueCategoriesView u
join Paper p on p.Categories like '%' || u.Category || '%'
group by u.Category;
