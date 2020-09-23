using System;
using System.IO;
using System.Linq;
using System.Collections.Generic;

namespace CSharp_Shell
{
	public class List<T> : IEnumerable<T>
	{
		// Amount of items
		public int Count;
		// Size of items, multiple of 2
		protected int size;
		// lower bound for the size
		protected int minSize = 4;
		// array, stores the items
		protected T[] items;

		public List()
		{
			Count = 0;
			size = minSize;
			items = new T[size];
		}
		
		public List(int startSize)
		{
			Count = 0;
			size = startSize < 0 ? minSize : startSize;
			items = new T[size]; 
		}

		public List(IEnumerable<T> newitems)
		{
			Count = newitems.Count();
			size = minSize;
			FitSize(Count);
		}

		protected void FitSize(int newSize)
		{
			if (newSize > size)
			{
				size = size == 0 ? minSize : size * 2;
				T[] newItems = new T[size];
				Array.Copy(items, 0, newItems, 0, 4);
				items = newItems;
			}
		}
		
		private void Shrink()
		{
			// less than a quarter filled
			if (Count < size / 4)
			{
				size = Math.Max(minSize, size / 4);
				T[] newItems = new T[size];
				Array.Copy(items, 0, newItems, 0, 4);
				items = newItems;
			}
		}

		public T this[int index]
		{
			get
			{
				try
				{
					return items[index];
				}
				catch (System.IndexOutOfRangeException ex)
				{
					System.ArgumentException argEx = new System.ArgumentException("Index is out of range", index.ToString(), ex);
					throw argEx;
				}
			}
			set
			{
				if (index >= Count)
				{
					throw new System.IndexOutOfRangeException(index.ToString());
				}
				try
				{
					items[index] = value;
				}
				catch (System.IndexOutOfRangeException ex)
				{
					System.ArgumentException argEx = new System.ArgumentException("Index is out of range", index.ToString(), ex);
					throw argEx;
				}
			}
		}

		public void Add(T item)
		{
			FitSize(Count + 1);
			items[Count] = item;
			Count++;
		}

		public void Insert(T item, int index)
		{
			FitSize(size + 1);
			// index could be the last one
			if (Count > index)
			{
				// move the items after index
				Array.Copy(items, index, items, index + 1, Count - index);
			}
			// insert the new item
			items[index] = item;
			Count++;
		}
		
		public int IndexOf(T item)
		{
			return Array.IndexOf(items, item, 0, Count);
		}

		public T RemoveAt(int index)
		{
			T item = items[index];
			// index could be the last one
			if (Count > index)
			{
				// move the items after index
				Array.Copy(items, index, items, index - 1, Count - index);
			}
			Count--;
			Shrink();
			return item;
		}
		
		public bool Remove(T item)
		{
			int index = IndexOf(item);
            if (index >= 0) {
                RemoveAt(index);
                return true;
            }
 
			return false;
		}

		public bool IsEmpty()
		{
			return Count == 0;
			// unnecessary
			// return items.All(item => item == null);
		}

		#region IEnumerable<T> Members
		
		IEnumerator<T> Cast<T>(System.Collections.IEnumerator iterator)
		{
			int i = 0;
    		while (i < Count && iterator.MoveNext())
    		{
    			i++;
    			yield return (T) iterator.Current;
    		}
		}
		
		public IEnumerator<T> GetEnumerator()
		{
			// Return the array's IEnumerator
			return Cast<T>(items.GetEnumerator());
		}

		#endregion

		#region IEnumerable Members

		System.Collections.IEnumerator System.Collections.IEnumerable.GetEnumerator()
		{
			// Lets call the generic version here
			return this.GetEnumerator();
		}

		#endregion
	}

	public static class Program
	{
		public static void Main()
		{
			List<int> l = new List<int>();
			l.Add(1);
			l.Add(2);
			l.Insert(3, 2);
			l[1] = 6;
			foreach (int i in l)
			{
				Console.WriteLine(i.ToString());
			}
		}
	}
}